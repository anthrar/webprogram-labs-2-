from flask import Blueprint, redirect, url_for, render_template, request, session
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


users = [
    {'login': 'alex', 'password': '123'},
    {'login': 'bob', 'password': '555'},
    {'login': 'paul', 'password': '777'},
    {'login': 'jack', 'password': '906'},
]

@lab4.route("/lab4/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab4/login.html', authorized = False)
    
    login = request.form.get('login')
    password = request.form.get('password')

    for user in users:
        if login == user['login'] and password == user['password']:
            return render_template('lab4/login.html', login = login, authorized = True)
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error = error, authorized = False)