from flask import Blueprint, render_template
from website import flatpages, POST_DIR

views = Blueprint('views',__name__)

@views.route('/')
def home():
  print("Hello")
  return render_template("home.html")

@views.route('/about')
def about():
  return render_template("about.html")

# @views.route('/blog')
# def blog():
#   return render_template("blog.html")

@views.route('/projects')
def projects():
  return render_template("projects.html")

@views.route("/blog/")
def posts():
    posts = [p for p in flatpages]
    print(posts)
    print(flatpages)
    # posts.sort(key=lambda item:item["date"], reverse=False)
    return render_template('blog.html', posts=posts)

@views.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)