from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
lab5 = Blueprint('lab5',__name__)

@lab5.route("/lab5/")
def lab():
    return render_template('lab5/lab5.html', login = session.get('login'))

def db_connect():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database = 'pavel_krasov_knowledge_base',
        user = 'pavel_krasov_knowledge_base',
        password = '777'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route("/lab5/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    if not (login or password):
        return render_template('lab5/register.html', error = 'Заполните поля!')
    
    conn, cur = db_connect()

    cur.execute(f"Select login From users Where login='{login}';")
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error = 'Такой пользователь уже существует!')
    
    password_hash = generate_password_hash(password)
    cur.execute(f"Insert into users (login, password) Values ('{login}', '{password_hash}');")
    
    db_close(conn, cur)
    return render_template('lab5/success.html', login=login)

@lab5.route("/lab5/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    if not (login or password):
        return render_template('lab5/login.html', error = 'Заполните поля!')
    
    conn, cur = db_connect()

    cur.execute(f"Select * From users Where login='{login}';")
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', error = 'Логин и/или пароль неверны.')
    
    if not check_password_hash (user['password'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html', error = 'Логин и/или пароль неверны.')
    
    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)


@lab5.route("/lab5/create", methods = ['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    if request.method == 'GET':
        return render_template('/lab5/create_article.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    
    conn, cur = db_connect()

    cur.execute("Select * From users Where login=%s;", (login, ))
    user_id = cur.fetchone()["id"]

    cur.execute(f"Insert into articles(user_id, title, article_text) \
                 Values ({user_id}, '{title}', '{article_text}');")
    
    db_close(conn, cur)
    return redirect('/lab5')


@lab5.route('/lab5/list')
def list():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    cur.execute(f"Select id From users Where login='{login}';")
    user_id = cur.fetchone()["id"]

    cur.execute(f"Select * From articles Where user_id='{user_id}';")
    articles = cur.fetchall()

    db_close(conn, cur)
    return render_template('/lab5/articles.html', articles=articles)



