from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route("/lab2/example")
def example():
    name = 'Павел'
    number = '2'
    group = 'ФБИ-23'
    course = '3'
    fruits = [
        {'name': 'манго', 'price': 100},
        {'name': 'арбузы', 'price': 120},
        {'name': 'бананы', 'price': 140},
        {'name': 'яблоки', 'price': 80}, 
        {'name': 'персики', 'price': 96}
    ]
    books = [
        {'author': 'Харлан Элисон','naming':'У меня нет рта, но я должен кричать', 'genre': 'постапокалиптика', 'pages': 10},
        {'author': 'Кормак Маккарти','naming':'Кровавый меридиан', 'genre': 'Вестерн', 'pages': 480},
        {'author': 'Дж. М. Кёсемен','naming':'Все грядущие дни', 'genre': 'Научная фантастика', 'pages': 308},
        {'author': 'Дж. К. Роулинг','naming':'Гарри Поттер и Кубок Огня', 'genre': 'Фэнтези, драма', 'pages': 704},
        {'author': 'Дрю Карпишин','naming':'Звёздные войны. Старая Республика: Реван', 'genre': 'Научная фантастика', 'pages': 298},
        {'author': 'Джордж Оруэлл','naming':'Скотный двор', 'genre': 'антиутопия, сатира', 'pages': 256},
        {'author': 'Джордж Оруэлл','naming':'1984', 'genre': 'антиутопия', 'pages': 320},
        {'author': 'Тимоти Зан','naming':'Траун', 'genre': 'Героическое зарубежное фэнтези ', 'pages': 480},
        {'author': 'Стивен Кинг','naming':'Кладбище Домашних животных', 'genre': 'Ужасы', 'pages': 373},
        {'author': 'Дж.Р.Р.Толкин','naming':'Сильмариллион', 'genre': 'Повесть', 'pages': 365}
    ]
    return render_template('lab2/example.html', name=name, number=number, group=group, course=course, fruits=fruits, books=books)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')

@lab2.route('/lab2/creatures')
def creatures():
    monsters = [
        {'name': 'Грифон', 'pic': 'грифон.jpeg', 'description': '''
            Грифоны — противоречивые существа, одновременно объединяющие Небеса и Землю.
         '''},
         {'name': 'Минотавр', 'pic': 'минотавр.jpg', 'description': '''
            Минота́вр  — по греческому преданию, чудовище с телом человека и головой быка.
         '''},
         {'name': 'Циклоп', 'pic': 'циклоп.jpg', 'description': '''
            Циклопы — одноглазые монстры, в разных версиях божественные существа или либо отдельный народ.
         '''},
         {'name': 'Бафомет', 'pic': 'бафомет.jpeg', 'description': '''
            Бафомет - божество знаний и мудрости у эзотериков и оккультистов.
         '''},
         {'name': 'Импундулу', 'pic': 'импундулу.jpeg', 'description': '''
            Импундулу — птица размером с человека, с мощными крыльями, из кончиков которых
            вылетают молнии, миф о которой распространен в Южной Африке
         '''}
    ]
    return render_template('lab2/creatures.html', monsters=monsters)