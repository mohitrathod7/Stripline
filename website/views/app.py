# Flask imports
from flask import Flask

# Database imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Built-In Imports
import os


template_dir = os.path.relpath('templates/', 'app.py')
static_dir = os.path.relpath('static/', 'app.py')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


# BASIC CONFIG
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../static/databases/database.db'


# RCAPTCHA CONFIG
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] ='6LcmFawcAAAAAI175JYBVdXy3pdls_l2degC7hDm'
app.config['RECAPTCHA_PRIVATE_KEY'] ='6LcmFawcAAAAAMqVSb06ZIe5eTLCwHKFP_iOqsbS'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'light'}
app.config['TESTING'] = True


# LOGIN MANAGER CONFIG
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.log_in'


@app.errorhandler(404)
# inbuilt function which takes error as parameter 
def not_found(e):
    return "error page"


db = SQLAlchemy(app)
