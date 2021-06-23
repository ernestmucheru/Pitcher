from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    return render_template('profile.html', username=username)
