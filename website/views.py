from flask import Blueprint, render_template
import markdown
from pathlib import Path
# from flask_flatpages import FlatPages
# from website import create_app
import os

# FLATPAGES_EXTENSION = '.md'
# FLATPAGES_ROOT = 'content'
# POST_DIR = 'blog_posts'

# flatpages = FlatPages(create_app)

views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template("home.html")

@views.route('/about')
def about():
  return render_template("about.html")

@views.route('/blog')
# def index():
#     # Get a list of all the markdown files in the content folder
#     posts = []
#     for filename in os.listdir("/website/content/blog_posts/"):
#         if filename.endswith(".md"):
#             with open(os.path.join("content", filename), "r") as f:
#                 # Parse the markdown file and extract the title and description
#                 content = f.read()
#                 html = markdown.markdown(content)
#                 title = html.split("<h1>")[1].split("</h1>")[0]
#                 description = html.split("<p>")[1].split("</p>")[0]
#             # Add the title, description, and filename to the list of projects
#             posts.append({
#                 "title": title,
#                 "description": description,
#                 "filename": filename
#             })
#     # Render the index.html template with the list of projects
#     return render_template("blog.html", posts=posts)
  
  
def blog():
  p = Path(os.path.join(os.path.dirname(__file__),'content','blog_posts'))
  blogfiles = p.glob('*.md')
  
  blogs = []
  if blogfiles.endswith(".md"):
    with open(blogfiles, "r") as f:
      # Parse the markdown file and extract the title and description
      content = f.read()
      html = markdown.markdown(content)
      title = html.split("<h1>")[1].split("</h1>")[0]
      description = html.split("<p>")[1].split("</p>")[0]
      # Add the title, description, and filename to the list of projects
    blogs.append({
      "title": title,
      "description": description,
      "filename": blogfiles
      })
    
  # posts = [p for p in blogfiles]
  return render_template("blog.html", posts=posts, location=p)

# def posts():
#   posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
#   posts.sort(key=lambda item:item['date'], reverse=False)
#   return render_template('blog.html', posts=posts)

# def post(name):
#   path = '{}/{}'.format(POST_DIR, name)
#   post = flatpages.get_or_404(path)
#   return render_template('post.html', post=post)

@views.route("/project/<filename>")
def project(filename):
    # Load the markdown file for the requested project
    with open(os.path.join("content", filename), "r") as f:
        content = f.read()
        # Convert the markdown to HTML and render the project.html template
        html = markdown.markdown(content)
        return render_template("post.html", html=html)
    
@views.route('/projects')
def projects():
  return render_template("projects.html")