from __future__ import annotations

import configparser
import os
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Dict

from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer


BASE_DIR = Path(__file__).resolve().parent


def _truthy(value: str | None) -> bool:
    if value is None:
        return False
    return value.lower() in {"1", "true", "t", "yes", "y"}


DEBUG = _truthy(os.getenv("FLASK_DEBUG", "false"))

CONFIG_KEYS = (
    "domain",
    "email",
    "your_name",
    "github",
    "blog_comments",
    "hubspot",
    "linkedin",
    "twitter",
)
CONFIG_SECTION = "configs"
CONFIG_FILE = Path(os.getenv("SITE_CONFIG_PATH") or BASE_DIR / "config.ini")


def create_app() -> Flask:
    app = Flask(
        __name__,
        static_folder=str(BASE_DIR / "static"),
        template_folder=str(BASE_DIR / "templates"),
    )

    app.config.update(
        FLATPAGES_AUTO_RELOAD=DEBUG,
        FLATPAGES_EXTENSION=".md",
        FLATPAGES_ROOT=str(BASE_DIR / "content"),
    )

    flatpages = FlatPages(app)
    freezer = Freezer(app)

    app.extensions["flatpages_instance"] = flatpages
    app.extensions["freezer_instance"] = freezer

    register_routes(app, flatpages)
    register_template_context(app)

    return app


def register_template_context(app: Flask) -> None:
    @app.context_processor
    def inject_global_variables() -> Dict[str, str | int]:
        site_config = _get_site_config()
        return {
            **site_config,
            "current_year": datetime.now().year,
        }


def register_routes(app: Flask, flatpages: FlatPages) -> None:
    DIR_BLOG_POSTS = "blogs"
    DIR_PROJECTS = "projects"


    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/resume")
    def resume():
        return render_template("resume.html")

    @app.route("/blog/")
    def posts():
        posts = [p for p in flatpages if p.path.startswith(DIR_BLOG_POSTS)]
        filtered_posts = [
            post
            for post in posts
            if getattr(post, "meta", {}).get("published") is True
        ]
        latest = sorted(
            filtered_posts,
            reverse=True,
            key=lambda p: getattr(p, "meta").get("date"),
        )
        return render_template("blog.html", posts=latest)

    @app.route("/post/<name>/")
    def post(name: str):
        path = f"{DIR_BLOG_POSTS}/{name}"
        post_page = flatpages.get_or_404(path)
        return render_template("blog-post.html", post=post_page)

    @app.route("/projects/")
    def projects():
        projects = [p for p in flatpages if p.path.startswith(DIR_PROJECTS)]
        latest = sorted(
            projects,
            reverse=True,
            key=lambda p: getattr(p, "meta").get("date"),
        )
        return render_template("projects.html", projects=latest)

    @app.route("/blog/search", methods=["POST"])
    def search_blog():
        query = request.form.get("query", "")
        if not query:
            posts = get_latest_posts(limit=10, flatpages=flatpages, directory=DIR_BLOG_POSTS)
        else:
            posts = search_posts(query, flatpages=flatpages, directory=DIR_BLOG_POSTS)
        return render_template("blog.html", posts=posts, query=query)


def search_posts(query: str, flatpages: FlatPages | None = None, directory: str = "blogs"):
    """Search through all flatpage blog posts and return posts that match the query."""
    flatpages = flatpages or app.extensions["flatpages_instance"]
    results = []

    posts = [p for p in flatpages if p.path.startswith(directory)]

    for post in posts:
        published_status = getattr(post, "meta", {}).get("published")
        if published_status is True:
            content_text = post.body
            if query.lower() in content_text.lower():
                results.append(post)

    return results


def get_latest_posts(limit: int = 10, flatpages: FlatPages | None = None, directory: str = "blogs"):
    """Retrieve the latest 'limit' blog posts."""
    flatpages = flatpages or app.extensions["flatpages_instance"]
    posts = [p for p in flatpages if p.path.startswith(directory)]
    filtered_posts = [
        post for post in posts if getattr(post, "meta", {}).get("published") is True
    ]
    latest = sorted(
        filtered_posts,
        reverse=True,
        key=lambda p: getattr(p, "meta").get("date"),
    )
    return latest[:limit]


@lru_cache(maxsize=1)
def _load_config_from_file():
    config = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE, encoding="utf-8")
    if config.has_section(CONFIG_SECTION):
        return dict(config.items(CONFIG_SECTION))
    return {}


def _get_site_config() -> Dict[str, str]:
    if DEBUG:
        _load_config_from_file.cache_clear()

    file_config = _load_config_from_file()
    resolved: Dict[str, str] = {}
    for key in CONFIG_KEYS:
        env_key = f"SITE_{key.upper()}"
        resolved[key] = os.getenv(env_key, file_config.get(key, "")).strip()
    return resolved


app = create_app()

flatpages: FlatPages = app.extensions["flatpages_instance"]
freezer: Freezer = app.extensions["freezer_instance"]


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=6000)
