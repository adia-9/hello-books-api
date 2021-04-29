from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__) #creating a new flask callled app

    from .routes import hello_world_bp #from file routes import variable hello-w...
    app.register_blueprint(hello_world_bp) 
    #register that var flask, so it knows to use this bluepr for our routes
    
    return app
