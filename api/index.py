from __future__ import annotations

import configparser
import os
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

from flask import Flask, Response, redirect, render_template, request, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer


BASE_DIR = Path(__file__).resolve().parent
BLOG_DIRECTORY = "blogs"
PROJECT_DIRECTORY = "projects"
CONFIG_KEYS = (
    "domain", "email", "your_name", "github", "blog_comments",
    "hubspot", "linkedin", "twitter",
)


def _is_truthy(value: str | None) -> bool:
    return bool(value and value.lower() in {"1", "true", "yes", "on"})


DEBUG = _is_truthy(os.getenv("FLASK_DEBUG"))
CONFIG_FILE = Path(os.getenv("SITE_CONFIG_PATH", BASE_DIR / "config.ini"))


@lru_cache(maxsize=1)
def _file_config() -> dict[str, str]:
    parser = configparser.ConfigParser()
    parser.read(CONFIG_FILE, encoding="utf-8")
    return dict(parser.items("configs")) if parser.has_section("configs") else {}


def site_config() -> dict[str, str]:
    if DEBUG:
        _file_config.cache_clear()
    defaults = _file_config()
    return {
        key: os.getenv(f"SITE_{key.upper()}", defaults.get(key, "")).strip()
        for key in CONFIG_KEYS
    }


def published_posts(flatpages: FlatPages):
    return [
        page for page in flatpages
        if page.path.startswith(f"{BLOG_DIRECTORY}/")
        and page.meta.get("published") is True
    ]


def newest(pages):
    return sorted(pages, reverse=True, key=lambda page: page.meta.get("date", ""))


def create_app() -> Flask:
    app = Flask(
        __name__,
        static_folder=BASE_DIR / "static",
        template_folder=BASE_DIR / "templates",
    )
    app.config.update(
        DEBUG=DEBUG,
        FLATPAGES_AUTO_RELOAD=DEBUG,
        FLATPAGES_EXTENSION=".md",
        FLATPAGES_ROOT=str(BASE_DIR / "content"),
    )

    flatpages = FlatPages(app)
    freezer = Freezer(app)
    app.extensions["flatpages_instance"] = flatpages
    app.extensions["freezer_instance"] = freezer

    @app.context_processor
    def template_context():
        config = site_config()
        domain = (
            config["domain"].removeprefix("https://")
            .removeprefix("http://").rstrip("/")
        )
        canonical_url = f"https://{domain}{request.path}" if domain else request.url
        return {
            **config,
            "canonical_url": canonical_url,
            "current_year": datetime.now(timezone.utc).year,
        }

    @app.after_request
    def security_headers(response: Response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault(
            "Permissions-Policy", "camera=(), microphone=(), geolocation=()"
        )
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        if request.is_secure or request.headers.get("X-Forwarded-Proto") == "https":
            response.headers.setdefault(
                "Strict-Transport-Security", "max-age=31536000; includeSubDomains"
            )
        return response

    @app.get("/")
    def home():
        return render_template("home.html")

    @app.get("/about")
    def about():
        return render_template("about.html")

    @app.get("/resume")
    def resume():
        return redirect("https://rxresu.me/dnell.personal/danienellcom", code=302)

    @app.get("/blog/")
    def posts():
        return render_template("blog.html", posts=newest(published_posts(flatpages)))

    @app.get("/post/<name>/")
    def post(name: str):
        page = flatpages.get_or_404(f"{BLOG_DIRECTORY}/{name}")
        if page.meta.get("published") is not True:
            return app.response_class(status=404)
        return render_template("blog-post.html", post=page)

    @app.get("/projects/")
    def projects():
        pages = [
            page for page in flatpages
            if page.path.startswith(f"{PROJECT_DIRECTORY}/")
        ]
        return render_template("projects.html", projects=newest(pages))

    @app.post("/blog/search")
    def search_blog():
        query = request.form.get("query", "").strip()
        pages = published_posts(flatpages)
        if query:
            lowered = query.casefold()
            pages = [
                page for page in pages
                if lowered in page.body.casefold()
                or lowered in str(page.meta.get("title", "")).casefold()
            ]
        return render_template("blog.html", posts=newest(pages)[:10], query=query)

    @app.get("/robots.txt")
    def robots():
        return Response(
            f"User-agent: *\nAllow: /\nSitemap: {url_for('sitemap', _external=True)}\n",
            mimetype="text/plain",
        )

    @app.get("/sitemap.xml")
    def sitemap():
        urls = [
            url_for("home", _external=True),
            url_for("about", _external=True),
            url_for("projects", _external=True),
            url_for("posts", _external=True),
        ]
        urls.extend(
            url_for(
                "post",
                name=page.path.removeprefix(f"{BLOG_DIRECTORY}/"),
                _external=True,
            )
            for page in published_posts(flatpages)
        )
        body = "".join(f"<url><loc>{url}</loc></url>" for url in urls)
        return Response(
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            f"{body}</urlset>",
            mimetype="application/xml",
        )

    return app


app = create_app()
flatpages: FlatPages = app.extensions["flatpages_instance"]
freezer: Freezer = app.extensions["freezer_instance"]


def search_posts(query: str):
    lowered = query.casefold()
    return [
        page for page in published_posts(flatpages)
        if lowered in page.body.casefold()
    ]


def get_latest_posts(limit: int = 10):
    return newest(published_posts(flatpages))[:limit]
