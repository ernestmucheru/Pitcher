from flask import render_template
from . import main
from flask_login import login_required,current_user
from ..models import Pitch, User, Upvote
import datetime
from .. import db

@main.route('/')
def home():
    def index():

        interview_pitches = Pitch.get_pitches('interview')
        product_pitches = Pitch.get_pitches('product')
        promotion_pitches = Pitch.get_pitches('promotion')
        
        return render_template('index.html', interview=interview_pitches, product=product_pitches, promotion=promotion_pitches)

@main.route('/about')
def about():
    return render_template('profile.html')
