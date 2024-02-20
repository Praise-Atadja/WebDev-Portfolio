from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
       return render_template("home.html", user=current_user)


@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
       return render_template("dashboard.html", user=current_user)

        
@views.route('/settings', methods=['GET','POST'])
def settings():
           return render_template('settings.html',  user=current_user)

@views.route('/profile', methods=['GET','POST'])
def profile():
           return render_template('profile.html',  user=current_user)

@views.route('/support', methods=['GET','POST'])
def support():
           return render_template('support.html',  user=current_user)




