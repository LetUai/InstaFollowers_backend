from flask import Flask 

def create_app():
    app = Flask(__name__)
    
    from .login import bp_login
    app.register_blueprint(bp_login)

    return app
