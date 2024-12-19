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
    login_user(user, remember=False)

    return redirect('/lab8/')

@lab8.route("/lab8/login", methods=['GET', 'POST'])
def login():        
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    remember = request.form.get('remember') == 1


    user = users.query.filter_by(login=login).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember= remember )
            return redirect('/lab8')
        
    return render_template('lab8/login.html', error = 'Логин и/или пароль неверны.')

@lab8.route("/lab8/logout")
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/articles', methods = ['GET'])
@login_required
def articles_list():
    q = request.args.get('q')
    search = bool(q) 
    q = q if q else ''
    qlike = q + '%' if q else '%'
    search_text = articles.article_text.like(qlike)
    articles_list = articles.query.filter(search_text).filter_by(is_public=True).all()
    if current_user.is_authenticated:
        articles_list = articles.query.filter(search_text).filter_by(login_id=current_user.id, is_public=False).all() + articles_list

    return render_template('lab8/articles.html', articles=articles_list, q=q, search = search) 


def loadArticleValues():
    r={}
    r['title'] = request.form.get('title')
    r['article_text'] = request.form.get('article_text')
    r['is_favorite'] = bool(request.form.get('is_favorite'))
    r['is_public'] = bool(request.form.get('is_public'))
    return r

@lab8.route("/lab8/create", methods = ['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        new_article = articles(title='', article_text='', is_favorite=False, is_public=True, likes=0)
        return render_template('lab8/create.html', article = new_article, action = url_for('lab8.create') )
    
    form_values = loadArticleValues()
    article = articles(**form_values)
    article.login_id = current_user.id

    db.session.add(article)
    db.session.commit()
    return render_template('lab8/create.html', article = article, message = 'Статья успешно создана', action = url_for('lab8.edit', id=article.id) )
    #return redirect('/lab8/articles')

@lab8.route("/lab8/edit/<int:id>", methods = ['GET', 'POST'])
@login_required 
def edit(id):
    article = articles.query.get_or_404(id)
    if not article:
        return redirect('/lab8/articles')
    
    if request.method == 'GET':
        return render_template('lab8/create.html', article = article)
    
    form_values = loadArticleValues()
    
    db.session.query(articles).filter( articles.id == id  ).update( form_values ) 
    db.session.commit()
    #db.refresh(article)
    return render_template('lab8/create.html', article = article, message = 'Успешно сохранена', action = url_for('lab8.edit', id=article.id) )

@lab8.route("/lab8/del/<int:id>", methods = ['GET', 'POST'])
@login_required
def delete(id):  
    item = articles.query.get_or_404(id)
    if not item:
        redirect ('/lab8/articles')
    db.session.delete(item)  # удаляем объект
    db.session.commit()     # сохраняем изменения  
    return render_template('lab8/delete_done.html')


