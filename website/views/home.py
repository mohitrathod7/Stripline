from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from website.models.tables import User


h = Blueprint('/', __name__)

@h.route('/')
def home():
    return redirect(url_for("/doctor.home"))
