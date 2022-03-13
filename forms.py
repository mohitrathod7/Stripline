# Form imports
from re import search
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import *
from wtforms.validators import InputRequired, Length, Email
from wtforms.fields.html5 import EmailField, DecimalField


# ---------------------------------------------- FORMS --------------------------------------------

class LoginForm(FlaskForm):
    type      = SelectField('Login as : ',    choices=[('user', 'Login as User'), ('doctor', 'Login as Doctor')])
    username  = StringField('Username : ',    validators=[InputRequired(message='Username is required'), Length(min=4, max=40, message="User name must be 4 to 16 characters long !!!")])
    password  = PasswordField('Password : ',  validators=[InputRequired(message='Password is required'), Length(min=8, max=80, message="Password must be minimum 8 characters long !!!")])
    remember  = BooleanField('Stay signed in')
    recaptcha = RecaptchaField()

class SignupForm(FlaskForm):
    type       = SelectField('Signup as : ',    choices=[('user', 'Sign up as User'), ('doctor', 'Sign up as Doctor')])
    username   = StringField('Username : ',   validators=[InputRequired(message='Username is required'),    Length(min=4, max=16, message="User name must be 4 to 16 characters long !!!")])
    password   = PasswordField('Password : ', validators=[InputRequired(message='Password is required'),    Length(min=8, max=80, message="Password must be minimum 8 characters long !!!")])
    firstname  = StringField('First name : ', validators=[InputRequired(message='First name is required'),  Length(min=4, max=20, message="First name must be 4 to 20 characters long !!!")])
    middlename = StringField('Last name : ',  validators=[InputRequired(message='Middle name is required'), Length(min=4, max=20, message="Middle name must be 4 to 20 characters long !!!")])
    lastname   = StringField('Last name : ',  validators=[InputRequired(message='Last name is required'),   Length(min=4, max=20, message="Last name must be 4 to 20 characters long !!!")])
    profile    = StringField('Profile : ',   validators=[InputRequired(message='Profile picture is required'),    Length(min=2, max=16, message="Profile picture must be 4 to 16 characters long !!!")])
    
class ChangePasswordForm(FlaskForm):
    pass
