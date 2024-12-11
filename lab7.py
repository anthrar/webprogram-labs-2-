from flask import Blueprint, render_template, request 
lab7 = Blueprint('lab7',  __name__ ) 

@lab7.route('/lab7/') 
def main(): 
    return render_template('lab7/index.html') 


films = [
    {
        'id': 1,
        'title': 'The Shawshank Redemption',
        'title_ru': 'Побег из Шоушенка',
        'year': 1994,
        'description': 'Бухгалтер Энди Дюфрейн обвинён в убийстве собственной жены и её любовника. Оказавшись в тюрьме под названием Шоушенк, он сталкивается с жестокостью и беззаконием, царящими по обе стороны решётки. Каждый, кто попадает в эти стены, становится их рабом до конца жизни. Но Энди, обладающий живым умом и доброй душой, находит подход как к заключённым, так и к охранникам, добиваясь их особого к себе расположения.',
    },
    {
        'id': 2,
        'title': 'The Godfather',
        'title_ru': 'Крестный отец',
        'year': 1972,
        'description': 'Криминальная сага, повествующая о нью-йоркской сицилийской мафиозной семье Корлеоне.'
    },
    {
        'id': 3,
        'title': 'Interstellar',
        'title_ru': 'Интерстеллар',
        'year': 2014,
        'description': 'Космический фильм о бесконечном пространстве, которое узнаёт свою судьбу после падения солнца.'
    },
    {
        'id': 4,
        'title': 'The Dark Knight',
        'title_ru': 'Темный Рыцарь',
        'year': 2008,
        'description': 'Бэтмен поднимает ставки в войне с криминалом. скоро они обнаружат себя посреди хаоса, развязанного восходящим криминальным гением, известным напуганным горожанам под именем Джокер'
    },
    ]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def films_list():
    return films


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id > len(films) or id < 0:
        return "Film not found", 404
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def delete_film(id):
    if id > len(films) or id < 0:
        return "Film not found", 404
    del films[id]
    return "", 204

