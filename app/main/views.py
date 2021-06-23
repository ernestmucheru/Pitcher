from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/user/<username>')
def user(username):
    return render_template('main/user.html', username=username)