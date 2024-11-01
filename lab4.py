from flask import Blueprint, redirect, url_for, render_template, request, session
import json
lab4 = Blueprint('lab4',__name__)

@lab4.route("/lab4/")
def lab():
    return render_template('lab4/lab4.html')

@lab4.route("/lab4/div-form")
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route("/lab4/div", methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 =='' or x2 == '':
        return render_template('lab4/div.html', error ='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error ='На ноль делить нельзя!')
    result = x1/x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route("/lab4/sum-form")
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route("/lab4/sum", methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 =='':
        x1 = '0' 
    if x2 == '':
        x2 = '0'
    x1 = int(x1)
    x2 = int(x2)
    result = x1+x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route("/lab4/multi-form")
def multi_form():
    return render_template('lab4/multi-form.html')

@lab4.route("/lab4/multi", methods = ['POST'])
def multi():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 =='':
        x1 = '1' 
    if x2 == '':
        x2 = '1'
    x1 = int(x1)
    x2 = int(x2)
    result = x1*x2
    return render_template('lab4/multi.html', x1=x1, x2=x2, result=result)

@lab4.route("/lab4/minus-form")
def minus_form():
    return render_template('lab4/minus-form.html')

@lab4.route("/lab4/minus", methods = ['POST'])
def minus():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 =='' or x2 == '':
        return render_template('lab4/minus.html', error ='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    result = x1-x2
    return render_template('lab4/minus.html', x1=x1, x2=x2, result=result)

@lab4.route("/lab4/exponen-form")
def exponen_form():
    return render_template('lab4/exponen-form.html')

@lab4.route("/lab4/exponen", methods = ['POST'])
def exponeb():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 =='' or x2 == '':
        return render_template('lab4/exponen.html', error ='Оба поля должны быть заполнены!')
    
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 or x2 == 0:
        return render_template('lab4/exponen.html', error ='Поля не могут быть нулевыми!')
    result = x1**x2
    return render_template('lab4/exponen.html', x1=x1, x2=x2, result=result)

tree_count = 0

@lab4.route("/lab4/tree", methods=['GET', 'POST'])
def tree():
    global tree_count
    cut_disabled = ''
    plant_disabled = ''
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation =='cut':
        tree_count -=1
    elif operation =='plant':
        tree_count +=1
    
    if tree_count<0:
        cut_disabled = 'disabled'
        return render_template('lab4/tree.html', error ='Счётчик не может быть отрицательным!', 
                               cut_disabled=cut_disabled)
    

    if tree_count>7:
        plant_disabled = 'disabled'
        return render_template('lab4/tree.html', error ='Счётчик не может быть больше трёх!', 
                               plant_disabled=plant_disabled)

    return redirect('/lab4/tree')


@lab4.route("/lab4/login", methods=['GET', 'POST'])
def login():
    with open("./users.json", "r") as f:
        users = json.load(f)
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = session['name']
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', login = login, authorized = authorized, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')

    if login =='':
        return render_template('lab4/login.html', error='Не введён логин')
    if password == '':
        return render_template('lab4/login.html', error='Не введён пароль')
    
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error = error, authorized = False, login_value = login)


@lab4.route("/lab4/logout", methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route("/lab4/fridge", methods=['GET', 'POST'])
def fridge_temp():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')
    
    temp = request.form.get('temp')
    if temp =='':
        return render_template('lab4/fridge.html', error = 'Ошибка: не задана температура')
    temp = int(temp)
    if temp<-12:
        return render_template('lab4/fridge.html', message = 'Не удалось установить температуру - слишком низкое значение')
    if temp>-1:
        return render_template('lab4/fridge.html', message = 'Не удалось установить температуру - слишком высокое значение')
    if temp>-12 and temp<-9:
        return render_template('lab4/fridge.html', temp=temp, message = f'Установлена температура:{temp}°C ❄❄❄')
    if temp>-8 and temp<-5:
        return render_template('lab4/fridge.html', temp=temp, message = f'Установлена температура:{temp}°C ❄❄')
    if temp>-4 and temp<-1:
        return render_template('lab4/fridge.html', temp=temp, message = f'Установлена температура:{temp}°C ❄')
    return render_template('lab4/fridge.html', temp=temp)


@lab4.route("/lab4/corn", methods=['GET', 'POST'])
def grain_order():
    if request.method == 'GET':
        return render_template('lab4/corn.html')

    corn = request.form.get('corn')
    weight = request.form.get('weight')

    if not weight:
        return render_template('lab4/corn.html', error='Пожалуйста, укажите вес заказа.')
    
    weight = float(weight)
    if weight <= 0:
        return render_template('lab4/corn.html', error='Вес заказа должен быть больше 0.')
    
    price_for_ton = {
            'ячмень': 12345,
            'овёс': 8522,
            'пшеница': 8722,
            'рожь': 14111
        }[corn]
    
    total_price = weight * price_for_ton

    if weight > 500:
        return render_template('lab4/corn.html', error='Такого объема зерна нет в наличии.')

    if weight > 50:
        discount = 0.1 * total_price
        total_price -= discount
        return render_template('lab4/corn.html', message=f'Заказ успешно сформирован. Вы заказали {weight} тонн {corn}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб. Применена скидка за большой объем - {discount:.2f} руб.')
    
    return render_template('lab4/corn.html', message=f'Заказ успешно сформирован. Вы заказали {weight} тонн {corn}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб.')


@lab4.route("/lab4/registration", methods=['GET', 'POST'])
def registration():
    with open("./users.json", "r") as f:
        users = json.load(f)
    if request.method == 'GET':
        return render_template('lab4/registration.html', users=users)
    
    login = request.form.get('login')
    password = request.form.get('password')
    name = request.form.get('name')
    sex = request.form.get('sex')
    
    if login =='':
        return render_template('lab4/registration.html', error='Не введён логин', login=login, password=password, name=name, sex=sex)
    if password == '':
        return render_template('lab4/registration.html', error='Не введён пароль', login=login, password=password, name=name, sex=sex)
    if name =='':
        return render_template('lab4/registration.html', error='Введите имя', login=login, password=password, name=name, sex=sex)
    if sex == '':
        return render_template('lab4/registration.html', error='Укажите свой пол', login=login, password=password, name=name, sex=sex)

    new_user = {'login': login, 'password': password, 'name': name, 'sex': sex}
    users.append(new_user)
    with open("./users.json", "w") as f:
        json.dump(users, f)
    session["login"] = login
    session['name'] = name
    return redirect('/lab4/edit_user')


@lab4.route("/lab4/del_user", methods=['GET', 'POST'])
def del_user():
    with open("./users.json", "r") as f:
        users = json.load(f)
    if 'login' not in session:
            return redirect('/lab4/login')
    
    login = session['login']
    new_users = []
    for user in users:
        if login != user['login']:
            new_users.append(user)
    users = new_users
    del session["login"]
    with open("./users.json", "w") as f:
        json.dump(users, f)
    return redirect('/lab4/registration')


@lab4.route("/lab4/edit_user", methods=['GET', 'POST'])
def edit_user():
    with open("./users.json", "r") as f:
        users = json.load(f)
    if 'login' not in session:
        return redirect('/lab4/login')
    if request.method == 'GET':
        user = next(u for u in users if u["login"] == session["login"])
        return render_template('lab4/edit.html', users=users, login=user["login"], password=user["password"], name=user["name"], sex=user["sex"])
    
    login = request.form.get('login')
    password = request.form.get('password')
    name = request.form.get('name')
    sex = request.form.get('sex')
    
    if login =='':
        return render_template('lab4/edit.html', error='Не введён логин', login=login, password=password, name=name, sex=sex)
    if password == '':
        return render_template('lab4/edit.html', error='Не введён пароль', login=login, password=password, name=name, sex=sex)
    if name =='':
        return render_template('lab4/edit.html', error='Введите имя', login=login, password=password, name=name, sex=sex)
    if sex == '':
        return render_template('lab4/edit.html', error='Укажите свой пол', login=login, password=password, name=name, sex=sex)
    
    new_users = []
    for user in users:
        if user["login"] == session["login"]:
            new_users.append({"login": login, "password": password, "name": name, "sex": sex})
        else:
            new_users.append(user)
    users = new_users
    session["login"] = login
    with open("./users.json", "w") as f:
        json.dump(users, f)

    return render_template('lab4/edit.html', users=users)


            
    
