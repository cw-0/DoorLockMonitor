from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField 
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError 

class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(5, 25),
            Regexp(r'^[A-Za-z0-9_]+$')
        ]
    )
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(8)
    ])
    confirm_password = PasswordField("Password", validators=[
        DataRequired(),
        Length(8)
    ])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(5, 25),
            Regexp(r'^[A-Za-z0-9_]+$')
        ]
    )
    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(8)
    ])
    submit = SubmitField("Login")
