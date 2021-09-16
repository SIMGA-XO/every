from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField,TextAreaField,validators
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired,Email


    
class SignupForm(FlaskForm):
    username=StringField("Name: ", validators=[DataRequired()])
    email=StringField("Email: ", validators=[Email()])
    password=PasswordField("Password: ", validators=[DataRequired(),
    validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit_regis = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[Email('Haba, enter email now')])
    password=PasswordField('Password',validators=[DataRequired('Your Password is a must')])
    
    remember = BooleanField('Agree?', validators=[DataRequired()])
    submit = SubmitField('Login')
