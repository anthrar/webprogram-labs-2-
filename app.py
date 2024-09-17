from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
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

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Красов Павел Андреевич, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <p>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename = 'lab1.css') + ''' " />
    </head>
    <body>
        <div class="oak">
            <h1>Дуб</h1>
            <img src="''' + url_for('static', filename = 'oak.jpg') + ''' ">
        </div>
    </body>
</html>
'''

