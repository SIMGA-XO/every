import mysql.connector
from projectapp import db

class Member(db.Model): 
    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    member_fname = db.Column(db.String(255), nullable=False)
    member_lname = db.Column(db.String(255), nullable=False)
    member_email = db.Column(db.String(255), nullable=False)
    member_phone = db.Column(db.String(255), nullable=False)
    member_pwd = db.Column(db.String(255), nullable=False)
    member_pix = db.Column(db.String(255), nullable=False)
    member_dob = db.Column(db.DateTime(), nullable=True)