from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>Красов Павел Андреевич, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2
        </header>

        <h1>web-сервер на flask</h1>

        <h2>Меню</h2>
        <ul>
        <li><a href = "/lab1">Первая лабораторная</a></li>
        </ul>
        <ul>
        <li><a href = "/lab2">Вторая лабораторная</a></li>
        </ul>
        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""