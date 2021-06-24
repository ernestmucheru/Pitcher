from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('profile.html')
