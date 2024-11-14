from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2
from psycopg2.extras import RealDictCursor
lab5 = Blueprint('lab5',__name__)

@lab5.route("/lab5/")
def lab():
    return render_template('lab5/lab5.html', login = session.get('login'))

@lab5.route("/lab5/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    if not (login or password):
        return render_template('lab5/register.html', error = 'Заполните поля!')
    
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database = 'pavel_krasov_knowledge_base',
        user = 'pavel_krasov_knowledge_base',
        password = '777'
    )
    cur = conn.cursor()

    cur.execute(f"Select login From users Where login='{login}';")
    if cur.fetchone():
        cur.close()
        conn.close()
        return render_template('lab5/register.html', error = 'Такой пользователь уже существует!')
    
    cur.execute(f"Insert into users (login, password) Values ('{login}', '{password}');")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('lab5/success.html', login=login)

@lab5.route("/lab5/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    if not (login or password):
        return render_template('lab5/login.html', error = 'Заполните поля!')
    
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database = 'pavel_krasov_knowledge_base',
        user = 'pavel_krasov_knowledge_base',
        password = '777'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"Select * From users Where login='{login}';")
    user = cur.fetchone()

    if not user:
        cur.close()
        conn.close()
        return render_template('lab5/login.html', error = 'Логин и/или пароль неверны.')
    
    if user['password'] != password:
        cur.close()
        conn.close()
        return render_template('lab5/login.html', error = 'Логин и/или пароль неверны.')
    
    session['login'] = login
    cur.close()
    conn.close()
    return render_template('lab5/success_login.html', login=login)