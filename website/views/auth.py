# Manual imports
import requests, os, random
from website.views.app import login_manager, db
from website.models.tables import User
from website.models.forms import LoginForm, SignupForm, ChangePasswordForm

# Flask imports
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user

# Form imports
from wtforms import *
from wtforms.validators import *

# Database imports
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


# --------------------------------------------- Sign up -------------------------------------------

@auth.route("/signup/", methods=["POST", "GET"])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():
        next_url = request.form.get("next")
    
        try:
            hashed_password = generate_password_hash(form.password.data, method='sha256')

            new_user =  User(
                            username   = form.username.data.lower(),
                            firstname  = form.firstname.data.lower().capitalize(),
                            middlename = form.middlename.data.lower().capitalize(),
                            lastname   = form.lastname.data.lower().capitalize(),
                            profile    = form.profile.data,
                            password   = hashed_password,
                            type       = form.type.data
                        )

            try:
                db.session.add(new_user)
                db.session.commit()

                if next_url:
                    flash("Successfully Signed up", "success")
                    return redirect(next_url)
                else:
                    flash("Successfully Signed up", "success")
                    return redirect(url_for('auth.log_in'))

            except:
                flash("This username already exists", "error")
                return render_template("pages/auth/signup.html", form=form)
        except:
            pass

        # flash here
        
    return render_template("pages/auth/signup.html", form=form)   
        

# --------------------------------------------- Log in --------------------------------------------

@auth.route("/login/", methods=["POST", "GET"])
def log_in():
    form = LoginForm()

    if form.validate_on_submit():
        next_url = request.form.get("next")
        user = User.query.filter_by(username=form.username.data.lower()).first()
        
        try:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                db.session.commit()

                if next_url:
                    flash("Successfully Logged in ", "success")
                    return redirect(next_url)
                else:
                    flash("Successfully Logged in ", "success")
                    if current_user.type == "user":
                        return redirect( url_for('/.home') )
                    else:
                        return redirect( url_for('/doctor.patients') )
            else:
                flash("The username or password is incorrect", "error")
                return render_template("pages/auth/login.html", form=form)
        except:
            pass
        flash("Couldn't find username", "error")

    return render_template("pages/auth/login.html", form=form)
    

# --------------------------------------------- Others --------------------------------------------

@auth.route("/logout")
@login_required
def log_out():
    db.session.commit()
    logout_user()

    flash("Successfully Logged out", "success")
    return redirect(url_for('/.home'))


@auth.route("/change-password")
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        next_url = request.form.get("next")
        user = User.query.filter_by(username=current_user.username).first()
        
        try:
            if check_password_hash(user.password, form.password.data):
                # check current password
                db.session.commit()

                if next_url:
                    flash("Password changed successfully", "success")
                    return redirect(next_url)
                else:
                    flash("Password changed successfully", "success")
                    return redirect( url_for('/h.home') )
            else:
                flash("The username or password is incorrect", "error")
                return render_template("pages/auth/password.html", form=form)
        except:
            pass

        flash("Couldn't change password", "success")
    return redirect(url_for('/.home'))


@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()
