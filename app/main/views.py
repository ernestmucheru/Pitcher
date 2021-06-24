from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models import Pitch, User, Upvote
import datetime
from .. import db
from .forms import PitchForm

@main.route('/')
def home():
    def index():

        interview_pitches = Pitch.get_pitches('interview')
        product_pitches = Pitch.get_pitches('product')
        promotion_pitches = Pitch.get_pitches('promotion')
        
        return render_template('index.html', interview=interview_pitches, product=product_pitches, promotion=promotion_pitches)

@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        title=pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        #pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user)

        #save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    title='New Pitch'
    return render_template('new_pitch.html', title=title,pitch_form=pitch_form)

@main.route('/pitches/interview_pitches')
def interview_pitches():
    pitches = Pitch.get_pitches('interview')

    return render_template('interview_pitches.html',pitches=pitches)

@main.route('/pitches/product_pitches')
def product_pitches():
    pitches = Pitch.get_pitches('product')

    return render_template('product_pitches.html',pitches=pitches)

@main.route('/pitches/promotion_pitches')
def product_pitches():
    pitches = Pitch.get_pitches('product')

    return render_template('promotion_pitches.html',pitches=pitches)




