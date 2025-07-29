from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(_name_)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

app =  Flask(__name__)
app.secret_key = 'supersecretmre'



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/servicepage')
def servicepage():
    return render_template('servicepage.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/registration.html')
def registration():
    return render_template('registration.html')


@app.route('/login')
def registerpage():
    return render_template('login.html')

@app.route('/bookappointmentdoctors')
def bookappointmentdoctors():
    return render_template('bookappointmentdoctors.html')



if __name__ =='__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)