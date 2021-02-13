import os, psycopg2
from flask import Flask, render_template, url_for, redirect,request,flash,session,jsonify
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
#app.config['SECRET_KEY'] = 'mysecret'
app.config['JSON_SORT_KEYS'] = False
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://dvlhxtkcgbtchj:f81260494b00ee325a7b68bb346d61a8dccf312bb59d9e539372b1b9c177ad7c@ec2-54-164-241-193.compute-1.amazonaws.com:5432/d5ddq76snvgm82"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



from server import route





        







