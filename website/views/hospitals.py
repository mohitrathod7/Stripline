from fileinput import hook_compressed
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from website.models.tables import User


hospitals = Blueprint('/hospitals', __name__)

@hospitals.route('/')
def home():
    return render_template("/pages/hospitals.html")
