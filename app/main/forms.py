from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    category = SelectField('Category', choices=[('interview', 'Interview Pitch'), ('product', 'Product Pitch'), ('promotion', 'Promotion Pitch')],validators=[Required()])
    submit = SubmitField('Post')