from flask import Blueprint, redirect, url_for, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

from db import db
from db.models import users, articles
from flask_login import login_required, login_user, current_user, logout_user

lab8 = Blueprint('lab8',__name__)

# routes
@lab8.route("/lab8/")
def lab():
    return render_template('lab8/lab8.html')

@lab8.route("/lab8/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    login_exists = users.query.filter_by(login=login).first()
    if login_exists:
        return render_template('lab8/register.html', error = 'Такой пользователь уже существует!')
    
    if login == '':
        return render_template('lab8/register.html', error = 'имя пользователя не должно быть пустым')
    if password == '':
        return render_template('lab8/register.html', error = 'пароль не должен быть пустым')

    password_hash = generate_password_hash(password)
    user = users(login=login, password=password_hash)   
    db.session.add(user)    
    db.session.commit()

    return redirect('/lab8/')

