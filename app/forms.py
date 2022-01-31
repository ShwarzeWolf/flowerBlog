from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class User_registration_form(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    passwordRepeatFieled = PasswordField("Password again: ", validators=[DataRequired()])
    submit = SubmitField("Submit")