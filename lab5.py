from flask import Blueprint, redirect, url_for, render_template, request, session
lab5 = Blueprint('lab5',__name__)

@lab5.route("/lab5/")
def lab():
    user_name = request.form.get('user_name')
    user_name = 'Anonumoys'
    return render_template('lab5/lab5.html', user_name=user_name)

