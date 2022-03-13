# Manual Imports
from datetime import datetime
from website.views.app import db
from website.models.relationships import *


# Database imports
from flask_login import UserMixin


# --------------------------------------------- TABLES --------------------------------------------

class User(UserMixin, db.Model):
    username    =  db.Column(db.String(15),   nullable=False,  primary_key=True)
    firstname   =  db.Column(db.String(20),   nullable=False)
    middlename  =  db.Column(db.String(20),   nullable=False)
    lastname    =  db.Column(db.String(20),   nullable=False)
    profile     =  db.Column(db.String(),     nullable=False)
    password    =  db.Column(db.String(80),   nullable=False)
    type        =  db.Column(db.String(10),   nullable=False)


    def __init__(self, username, firstname, middlename, lastname, profile, password, type):
        self.username   =  username
        self.firstname  =  firstname
        self.middlename =  middlename
        self.lastname   =  lastname
        self.profile    =  profile
        self.password   =  password
        self.type       =  type

    def get_id(self):
        return (self.username)
