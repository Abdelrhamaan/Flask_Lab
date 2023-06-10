from flask import Flask
from blog.config import proj_config
from blog.models import db , blog_post




def create_app(config_mode):
    app = Flask(__name__)
    app_config = proj_config[config_mode]

    app.config["SQLALCHEMY_DATABASE_URI"] = app_config
    app.config.from_object(app_config)
    db.init_app(app)
    from blog.posts.myBlueprints import posts_blueprint
    app.register_blueprint(posts_blueprint)
    return  app