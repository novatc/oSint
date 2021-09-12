from flask import Flask

from os import path


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ddf3Dkf79s0'
  

    from .homepage import homepage


    app.register_blueprint(homepage, url_prefix='/')


    return app
