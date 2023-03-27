import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

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


@app.route('/projects')
def projects():
  return render_template("projects.html")


# @app.route('/blog')
# def blog():
#   return render_template("blog.html")

@app.route("/blog/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    # posts.sort(key=lambda item:item["date"], reverse=False)
    return render_template('blog.html', posts=posts)

@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


app.run(debug=True,port=9000)
