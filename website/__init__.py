from flask import Flask
from flaskext.markdown import Markdown

def create_app():
  app = Flask(__name__)
  Markdown(app)
  
  from .views import views
  app.register_blueprint(views, url_prefix='/')
  
  return app
