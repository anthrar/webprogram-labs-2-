from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""

