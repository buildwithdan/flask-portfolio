from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from datetime import datetime
from functools import lru_cache
from pathlib import Path
import configparser
import os
import re


def _truthy(value: str | None) -> bool:
    if value is None:
        return False
    return value.lower() in {"1", "true", "t", "yes", "y"}


DEBUG = _truthy(os.getenv("FLASK_DEBUG", "false"))
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
DIR_BLOG_POSTS = 'blogs'
DIR_PROJECTS = 'projects'


CONFIG_KEYS = (
    'domain',
    'email',
    'your_name',
    'github',
    'blog_comments',
    'hubspot',
    'linkedin',
    'twitter',
)
CONFIG_SECTION = 'configs'
CONFIG_FILE = Path(os.getenv('SITE_CONFIG_PATH', Path(__file__).resolve().parent / 'config.ini'))


app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)
# app.config['SERVER_NAME'] = '0.0.0.0:6000'


# this context processors allows the below variables to be used in all templates, and you dont need to define it in each.
@app.context_processor
def inject_global_variables():
    site_config = _get_site_config()
    return {
        **site_config,
        'current_year': datetime.now().year,
    }


@app.route('/')
def home():
  return render_template("home.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/resume')
def resume():
  return render_template("resume.html")

@app.route("/blog/")
def posts():
    # Retrieve the posts
    posts = [p for p in flatpages if p.path.startswith(DIR_BLOG_POSTS)]
    # print("check1",posts)
    
    filtered_posts = []
    for post in posts:
        published_status = getattr(post, "meta").get('published')
        # print(f"Check2 - Published status for {post.path}: {published_status}")
        if published_status == True:
            filtered_posts.append(post)
    # print("check3", filtered_posts)
    
    # Sort the filtered posts by date
    latest = sorted(filtered_posts, reverse=True, key=lambda p: getattr(p, "meta").get('date'))
    # print("check4",latest)

    # Render the template with the sorted posts
    return render_template('blog.html', posts=latest)


@app.route('/post/<name>/')
def post(name):
    path = '{}/{}'.format(DIR_BLOG_POSTS, name)
    post = flatpages.get_or_404(path)
    return render_template('blog-post.html', post=post)
  
@app.route('/projects/')
def projects():
  projects = [p for p in flatpages if p.path.startswith(DIR_PROJECTS)]
  # Sort the filtered posts by date
  latest = sorted(projects, reverse=True, key=lambda p: getattr(p, "meta").get('date'))

  # Render the template with the sorted projects
  return render_template('projects.html', projects=latest)


# @app.route('/projects/<name>/')
# def project(name):
#     path = '{}/{}'.format(DIR_PROJECTS, name)
#     project = flatpages.get_or_404(path)
#     return render_template('projects-post.html', project=project)

# testing the search function for blogs

@app.route('/blog/search', methods=['POST'])

def search_blog():
    query = request.form.get('query')
    if not query:  # If the search query is empty
        posts = get_latest_posts(10)  # Get the last 10 posts
    else:
        posts = search_posts(query)
    return render_template('blog.html', posts=posts, query=query)
  
def search_posts(query):
    """Search through all flatpage blog posts and return posts that match the query."""
    results = []

    posts = [p for p in flatpages if p.path.startswith(DIR_BLOG_POSTS)]
    
    for post in posts:
        published_status = getattr(post, "meta").get('published')
        if published_status == True:
            content_text = post.body
            if query.lower() in content_text.lower():
                results.append(post)
    
    return results



def get_latest_posts(limit=10):
    """Retrieve the latest 'limit' blog posts."""
    posts = [p for p in flatpages if p.path.startswith(DIR_BLOG_POSTS)]
    filtered_posts = [post for post in posts if getattr(post, "meta").get('published') == True]
    latest = sorted(filtered_posts, reverse=True, key=lambda p: getattr(p, "meta").get('date'))
    return latest[:limit]


@lru_cache(maxsize=1)
def _load_config_from_file():
    config = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE, encoding='utf-8')
    if config.has_section(CONFIG_SECTION):
        return dict(config.items(CONFIG_SECTION))
    return {}


def _get_site_config():
    if DEBUG:
        _load_config_from_file.cache_clear()

    file_config = _load_config_from_file()
    resolved = {}
    for key in CONFIG_KEYS:
        env_key = f"SITE_{key.upper()}"
        resolved[key] = os.getenv(env_key, file_config.get(key, '')).strip()
    return resolved

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=6000)
