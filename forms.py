from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GreetingForm(FlaskForm):
    username = StringField("Your name", validators=[DataRequired()])
    submit = SubmitField("Greet")

