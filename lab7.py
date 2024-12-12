from flask import Blueprint, render_template, request, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path
lab7 = Blueprint('lab7',  __name__ ) 

# database
DBS = '?'
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

films = []
def getFilmList():
    global films

    conn, cur = db_connect()
    cur.execute("Select * From films order by id")
    films = cur.fetchall()    
    db_close(conn, cur)
    return films

def getFilmByID(id):
    conn, cur = db_connect()
    cur.execute("Select * From films where id = " + DBS + ";", (id, ))
    film = cur.fetchone()    
    db_close(conn, cur)
    
    return film

def updateFilm(film):
    conn, cur = db_connect()
    cur.execute("update films set title=" + DBS + ", title_ru=" + DBS + ", year=" + DBS + ", description=" + DBS + 
                   " where id=" + DBS + ";",
                (film['title'],film['title_ru'],film['year'],film['description'],film['id'],)  )
    conn.commit()
    db_close(conn, cur)

def deleteFilm(id):
    conn, cur = db_connect()
    cur.execute("Delete From films Where id=" + DBS + ";", (id, ))
    conn.commit()
    db_close(conn, cur) 

def insertFilm(film):
    conn, cur = db_connect()
    cur.execute("insert into films  (title, title_ru, year, description)  Values (" + DBS + "," + DBS + "," + DBS + "," + DBS + 
                    ");",
                (film['title'],film['title_ru'],film['year'],film['description'],)  )
    conn.commit()
    db_close(conn, cur)


@lab7.route('/lab7/') 
def main(): 
    return render_template('lab7/index.html') 


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def films_list():
    films = getFilmList()
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    film = getFilmByID(id)
    if not film:
        return "Film not found", 404
    return film

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def delete_film(id):
    deleteFilm(id)
    return "", 204

# проверки
# название (на оригинальном языке) — должно быть непустым, если и рус- ское название пустое;
# русское название — должно быть непустым;
# год—должен быть больше 1895  до текущего;
# описание — должно быть непустым, но не более 2000 символов.

def check(film):
    errors = {}
    if film['description'] == '':
        errors['description']= 'Заполните описание'
    if len(film['description']) > 2000:
        errors['description']= 'Описание должно быть не более 2000 символов'
    if film['title_ru'] == '':
        errors['title_ru']='Заполните название на русском'

    if film['title'] == '' and film['title_ru'] != '':
        film['title'] = film['title_ru']

    if int(film['year']) < 1895:
        errors['year']= 'Год должен быть больше 1895'
    if int(film['year'])     > 2024:
        errors['year']= 'Год должен быть не больше 2024'
    return errors, film

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    
    film = request.get_json()
    film['id'] = id

    errors, film = check(film)
    if errors:
        return errors, 400

    #films[id] = film
    updateFilm(film)
    return film

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film(): 
    film = request.get_json()

    errors, film = check(film)
    if errors:
        return errors, 400

    #films.append(film)  
    insertFilm(film)
    return "Success", 201
