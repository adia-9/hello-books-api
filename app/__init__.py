from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#creating a SQLAL db object
db = SQLAlchemy()
migrate = Migrate()
#postgresql+psycopg2://postgres:postgres@localhost:5432/ada_book

def create_app(test_config=None):
    app = Flask(__name__) #creating a new flask callled app

    #DB config
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/ada_book"
    
    db.init_app(app) #Init SQLAL obj,say this is the app you're gonna work with
    migrate.init_app(app, db) #app I want to work with 
    from app.models.book import Book #make my class visible


    from .routes import hello_world_bp #from file routes import variable hello-w...
    app.register_blueprint(hello_world_bp) 
    #register that var flask, so it knows to use this bluepr for our routes
    
    return app
