from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from website.models.tables import User


doctors = Blueprint('/doctor', __name__)

@doctors.route('/')
def home():
    doctors = User.query.filter_by(type="doctor").all()
    return render_template("/pages/doctors.html", doctors=doctors)


@doctors.route('/<doctor_username>')
def profile(doctor_username):
    doctor = User.query.filter_by(username=doctor_username).first()
    return render_template("/pages/doctorsProfile.html", doctor=doctor)

    
@doctors.route('/<doctor_username>/appointment')
def appointment(doctor_username):
    doctor = User.query.filter_by(username=doctor_username).first()
    # return render_template("/pages/doctorsProfile.html", doctor=doctor)
    return "appointment"

        
@doctors.route('/patients')
def patients():
    return render_template("/pages/patients.html")