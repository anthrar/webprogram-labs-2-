from flask import Blueprint, redirect, url_for, render_template, request, session, current_app
from lab9grats import getGrats, choice1, choice2

lab9 = Blueprint('lab9',__name__)


@lab9.route("/lab9/")
def main():
        return render_template('lab9/index.html')

# tag задает текущий шаг - какие данные нужно собирать
# tag = 'name' - собираем имя и т.д 
@lab9.route("/lab9/step/<tag>", methods=["POST"])
def step(tag):

    # шаги в том порядке как будут показываться формы
    tag_step = ['name', 'age', 'gender', 'choice1', 'choice2']

    # незнакомые теги игнорируем
    if tag not in tag_step:
        return redirect(url_for('lab9.index'))

    # храним данные в сессии, в словарике user, если его нет, значит создаем пустой
    user = session['user'] if 'user' in session else {}

    # если форма была отправлена c пустым значением то повторим вывод формы
    if tag in request.form:
        user[tag] = request.form[tag] 
        session['user'] = user

        # определяем текущий шаг
        step = tag_step.index(tag)

        # если мы дошли до конца, то выдаем поздравление
        if step + 1 >= len(tag_step):
            return redirect(url_for('lab9.show_grats'))

        # определяем следующий тег 
        nexttag = tag_step[step+1]
    else:
        nexttag = tag

    # для некоторых шагов собираем выбор
    if nexttag == 'choice1':
        choice = choice1
    elif nexttag == 'choice2':
        choice_all = choice2
        # выбор второго шага зависит от выбора первого
        choice = choice_all[user['choice1']]
    else:
        choice = ''

    # выбор теплейта задаем через переменную nexttag 
    return render_template(f'lab9/step_{nexttag}.html', user = session['user'], choice = choice )

    

@lab9.route("/lab9/grats", methods=["GET"])
def show_grats():
    if 'user' in session:
        user = session['user']
        return render_template(f'lab9/grats.html', user=user , grats = getGrats(user))
    else:
        return redirect(url_for('lab9.index'))
