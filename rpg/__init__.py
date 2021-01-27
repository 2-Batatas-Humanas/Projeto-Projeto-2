import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    rpg = Flask(__name__, instance_relative_config=True)
    rpg.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(rpg.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        rpg.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        rpg.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(rpg.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @rpg.route('/')
    def home():
        return render_template('index.html')

    from . import db
    db.init_app(rpg)

    from . import auth
    rpg.register_blueprint(auth.bp)

    return rpg