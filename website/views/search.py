from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from website.models.tables import User


search = Blueprint('search', __name__)

@search.route('/')
def home():
    return render_template("/pages/home.html")