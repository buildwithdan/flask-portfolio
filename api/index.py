from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
DIR_BLOG_POSTS = 'posts'
DIR_PROJECTS = 'projects'


app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route("/blog/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(DIR_BLOG_POSTS)]
    # posts.sort(key=lambda item:item["date"], reverse=False)
    return render_template('blog.html', posts=posts)

@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(DIR_BLOG_POSTS, name)
    post = flatpages.get_or_404(path)
    return render_template('blog-post.html', post=post)
  
@app.route('/projects/')
def projects():
  projects = [p for p in flatpages if p.path.startswith(DIR_PROJECTS)]
  return render_template("projects.html", projects=projects)

@app.route('/projects/<name>/')
def project(name):
    path = '{}/{}'.format(DIR_PROJECTS, name)
    project = flatpages.get_or_404(path)
    return render_template('projects-post.html', project=project)