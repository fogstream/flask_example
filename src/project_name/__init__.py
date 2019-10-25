from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project_name.config import configure_app

db = SQLAlchemy()


def create_app(import_name: str, config_name: str = 'default'):
    app = Flask(import_name)
    configure_app(app, config_name=config_name)
    db.init_app(app)
    return app
