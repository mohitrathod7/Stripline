from flask import Blueprint, render_template
from flask.helpers import flash
from flask_login import login_required, current_user

user = Blueprint('user', __name__)


@user.route("/")
@login_required
def home():
    if current_user.is_authenticated == True:
        return render_template("pages/home.html")
    else:
        flash("Log in to view", "error")
        return render_template("pages/home.html")