from flask import Flask
from flask_flatpages import FlatPages

flatpages = None

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

def create_app():
  app = Flask(__name__)
  
  global flatpages
  flatpages = FlatPages(app)
  
  from .views import views
  app.register_blueprint(views, url_prefix='/')
  
  return app
