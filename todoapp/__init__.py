from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from todoapp.config import Config

db = SQLAlchemy()

def create_app(config=Config):
    # TODO
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    from todoapp.main.routes import main
    app.register_blueprint(main)

    return app
