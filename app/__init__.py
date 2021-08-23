from flask import Flask

my_app = Flask(__name__)

from app.main import main as main_blueprint
my_app.register_blueprint(main_blueprint)

from app.src import src as src_blueprint
my_app.register_blueprint(src_blueprint)