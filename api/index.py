from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from datetime import datetime
import configparser

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
DIR_BLOG_POSTS = 'blogs'
DIR_PROJECTS = 'projects'


app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

# this context processors allows the below variables to be used in all templates, and you dont need to define it in each.
@app.context_processor
def inject_global_variables():
    config = configparser.ConfigParser()
    config.read('api/config.ini')

    # Access the variables in the "configs" section
    domain = config['configs']['domain']
    email = config['configs']['email']
    your_name = config['configs']['your_name']
    github = config['configs']['github']
    blog_comments = config['configs']['blog_comments']
    hubspot = config['configs']['hubspot']
    linkedin = config['configs']['linkedin']
    twitter = config['configs']['twitter']
    current_year = datetime.now().year

    return {
        'domain': domain,
        'email': email,
        'your_name': your_name,
        'github': github,
        'blog_comments': blog_comments,
        'hubspot': hubspot,
        'linkedin': linkedin,
        'twitter': twitter,
        'current_year': current_year
    }


@app.route('/')
def home():
  return render_template("home.html")

@app.route('/about')
def about():
  return render_template("about.html")

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
  return render_template("projects.html", projects=projects)

@app.route('/projects/<name>/')
def project(name):
    path = '{}/{}'.format(DIR_PROJECTS, name)
    project = flatpages.get_or_404(path)
    return render_template('projects-post.html', project=project)
