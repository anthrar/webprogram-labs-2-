from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('/lab3/lab3.html', name=name, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'green')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name')
    resp.set_cookie('age')
    resp.set_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    #Кофе стоит 120 рублей, чёрный чай - 80 рублей, зелёный - 70 рублей
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
    
    #Добавка молока удорожает напиток на 30 рублей, сахара - на 10
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    
    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    if color:
        resp = make_response(redirect('/lab3/settings.html'))
        resp.set_cookie('color', color)
        return resp

    color = request.cookies.get('color')
    resp = make_response(render_template('lab3/settings.html', color=color))
    return resp

@lab3.route('/lab3/form_rjd')
def form_rjd():
    errors = {}
    user = request.args.get ('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get ('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    place = request.args.get ('place')
    if place == '':
        errors['place'] = 'Заполните поле!'
    departure = request.args.get ('departure')
    if departure == '':
        errors['departure'] = 'Заполните поле!'
    arrival = request.args.get ('arrival')
    if arrival == '':
        errors['arrival'] = 'Заполните поле!'
    date = request.args.get ('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    return render_template('lab3/form_rjd.html', user=user, age=age, place=place, 
                           departure=departure, arrival=arrival, date=date, errors=errors)

@lab3.route('/lab3/ticket')
def ticket():
    user = request.args.get('user')
    departure = request.args.get('departure')
    arrival = request.args.get('arrival')
    date = request.args.get('date')
    underwear = request.args.get('underwear')
    luggage = request.args.get('luggage')
    belay = request.args.get('belay')
    price = 0
    age = int(request.args.get('age'))
    if age < 18:
        price = 700
    else:
        price = 1000

    place = request.args.get('place')
    if place == 'side_low':
        price += 100
        place = 'нижняя боковая'
    elif place == 'low':
        price += 100
        place = 'нижняя'
    elif place == 'up':
        price += 0
        place = 'верхняя'
    else:
        price += 0
        place = 'верхняя боковая'

    if request.args.get('underwear') == 'on':
        price += 75
    if request.args.get('luggage') == 'on':
        price += 250
    if request.args.get('belay') == 'on':
        price += 150

    return render_template('lab3/ticket.html', price=price, user=user, age=age, 
                           place=place, departure=departure, arrival=arrival, date=date, 
                           underwear=underwear, luggage=luggage, belay=belay)