from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])

    submission = SubmitField("Sign Up")

class LoginForm(FlaskForm):


    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=30)])

    remember_user = BooleanField("Remember Me")

    submission = SubmitField("Login")