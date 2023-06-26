from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from .models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_check):
        user = User.query.filter_by(username=username_check.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose another.')

    def validate_email(self, email_check):
        user = User.query.filter_by(email=email_check.data).first()
        if user:
            raise ValidationError('Email already taken. Please choose another.')

    username = StringField(label='Username', validators=[Length(min=4, max=25), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1', message='Passwords must match'), DataRequired()])
    submit = SubmitField(label='Sing up')


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=4, max=25), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    submit = SubmitField(label='Sing in')
