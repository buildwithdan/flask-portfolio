from flask import Flask
from flaskext.markdown import Markdown
from flask_flatpages import FlatPages

def create_app():
  app = Flask(__name__)
  Markdown(app)
  FlatPages(app)
  
  from .views import views
  app.register_blueprint(views, url_prefix='/')
  
  return app
