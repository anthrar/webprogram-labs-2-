from flask import Flask, redirect, url_for, render_template
import os
from os import path

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager


app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY ', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'pavel_krasov_orm'
    db_user = 'pavel_krasov_orm'
    db_password = '777'
    host_ip = '127.0.0.1'
    host_port = '5432'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "pavel_krasov_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db.init_app(app)



app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)



@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)
