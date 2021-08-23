from . import main
from flask import render_template

"""Main route to home page"""
@main.route("/")
def home():
    return render_template('index.html')

