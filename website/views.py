from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template("home.html")

@views.route('/about')
def about():
  return render_template("about.html")

@views.route('/blog')
def blog():
  return render_template("blog.html")

@views.route('/projects')
def projects():
  return render_template("projects.html")