from flask import Blueprint, redirect, url_for, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path
lab5 = Blueprint('lab5',__name__)

DBS = '?'

@lab5.route("/lab5/")
def lab():
    return render_template('lab5/lab5.html', login = session.get('login'))

def db_connect():
    global DBS
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'pavel_krasov_knowledge_base',
            user = 'pavel_krasov_knowledge_base',
            password = '777'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        DBS = '%s'
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    
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

    cur.execute("Select * From users Where login=" + DBS + ";", (login,))
    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error = 'Такой пользователь уже существует!')
    
    password_hash = generate_password_hash(password)
    cur.execute("Insert into users (login, password) Values (" + DBS + ", " + DBS + ");", (login, password_hash))
    
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

    cur.execute("Select * From users Where login=" + DBS + ";", (login,))
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

@lab5.route('/lab5/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab5/login')

@lab5.route("/lab5/create", methods = ['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    if request.method == 'GET':
        return render_template('/lab5/create_article.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    if title == '':
        return render_template('/lab5/create_article.html', error = 'Статьи без названий быть не может')
    if article_text == '':
        return render_template('/lab5/create_article.html', error = 'Ничего не написано')
    conn, cur = db_connect()

    cur.execute("Select * From users Where login=" + DBS + ";", (login, ))
    user_id = cur.fetchone()["id"]

    cur.execute("Insert into articles(user_id, title, article_text) \
                 Values (" + DBS + ", " + DBS + ", " + DBS + ");", (user_id, title, article_text))
    
    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/delete', methods=['GET', 'POST'])
def delete():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    id = request.args.get('id')

    conn, cur = db_connect()

    cur.execute("Delete From articles Where id=" + DBS + ";", (id, ))

    conn.commit()
    db_close(conn, cur)

    return render_template('/lab5/delete_done.html')

@lab5.route('/lab5/list')
def list():
    login = session.get('login')

    conn, cur = db_connect()

    if login:
        cur.execute("Select id From users Where login=" + DBS + ";", (login, ))
        user_id = cur.fetchone()["id"]
        cur.execute("Select * From articles Where is_public \
                    union \
                    Select * From articles Where user_id=" + DBS + " order by is_favorite;", (user_id, ))
    else:
        cur.execute("Select * From articles Where is_public order by is_favorite;")
    
    articles = cur.fetchall()

    db_close(conn, cur)

    has_articles = len(articles)

    return render_template('/lab5/articles.html', articles=articles, has_articles=has_articles)


@lab5.route('/lab5/edit', methods=['GET', 'POST'])
def edit():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        id = request.args.get('id')
        if id =='':
            return redirect('/lab5/list')
        
        conn, cur = db_connect()
        cur.execute("Select * From articles where id=" + DBS + ";", (id, )) 
        article = cur.fetchone()
        db_close(conn, cur)

        if article is None:
            AssertionError("article is ", article)
            return redirect('/lab5/list')
        
        return render_template('/lab5/edit_article.html', article=article)
    #post method
    id = request.form.get('id')
    title = request.form.get('title')
    is_favorite = request.form.get('is_favorite')
    is_public = request.form.get('is_public')
    article_text = request.form.get('article_text')
    if title == '':
        return render_template('/lab5/edit_article.html', error = 'Статьи без названий быть не может')
    if article_text == '':
        return render_template('/lab5/edit_article.html', error = 'Ничего не написано')
    
    conn, cur = db_connect()

    cur.execute("Update articles SET title=" + DBS + ", article_text=" + DBS + ",  \
                 is_favorite=" + DBS + ", is_public=" + DBS + " \
                    where id=" + DBS + ";", (title, article_text, is_favorite, 
                                            is_public, id))
    conn.commit()
    
    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/reg_users')
def reg_users():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')
    
    conn, cur = db_connect()

    cur.execute("Select * From users;")
    users = cur.fetchall()

    db_close(conn, cur)

    return render_template('/lab5/reg_users.html', users=users)

   
    


