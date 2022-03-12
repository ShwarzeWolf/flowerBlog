from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class User_registration_form(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    passwordRepeatFieled = PasswordField("Password again: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class User_login_form(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class Comment_creation_form(FlaskForm):
    content = StringField("Content: ", validators=[DataRequired()])
    submit = SubmitField("Submit")