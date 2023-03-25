from flask import Blueprint, render_template
from pathlib import Path
import os 

views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template("home.html")

@views.route('/about')
def about():
  return render_template("about.html")

@views.route('/blog')
def blog():
  p = Path(os.path.join(os.path.dirname(__file__),'content','blog_posts'))
  blogfiles = p.glob('*.md')
  posts = [p for p in blogfiles]
  
  return render_template("blog.html", posts1=posts)

@views.route('/projects')
def projects():
  return render_template("projects.html")