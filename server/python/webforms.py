from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class SignupForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    submit = SubmitField("Submit")

class ContactForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    message = TextAreaField("Message", widget = TextArea(), validators = [DataRequired()])
    submit = SubmitField("Submit")
