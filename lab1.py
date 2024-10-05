from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)


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


@lab1.route("/lab1/")
def lab():
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

        <ol>
        <li><a href = "/menu">Меню</a></li>
        </ol>

        <h2>Реализованные руты</h2>
        <ul>
        <li><a href = "/lab1/oak">Дуб</a></li>
        <li><a href = "/lab1/student">Студент</a></li>
        <li><a href = "/lab1/python">Python</a></li>
        <li><a href = "/lab1/legend">Легенда о девятихвостой лисе</a></li>
        </ul>

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <title>Красов Павел Андреевич, лабораторная 1</title>
            <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename = 'lab1.css') + ''' " />
    </head>
    <body>
        <header>
            НГТУ, ФБ, лабораторная работа 1
        </header>

        <div class="oak">
            <h1>Дуб</h1>
            <img src="''' + url_for('static', filename = 'oak.jpg') + ''' ">
        </div>

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Красов Павел Андреевич, лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename = 'lab1.css') + ''' " />
    </head>
    <body>
        <header>
            НГТУ, ФБ, лабораторная работа 1
        </header>

        <p>Красов Павел Андреевич</p>
            <img src="''' + url_for('static', filename = 'лого НГТУ.jpeg') + ''' ">

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Красов Павел Андреевич, лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename = 'lab1.css') + ''' " />
    </head>
    <body>
        <header>
            НГТУ, ФБ, лабораторная работа 1
        </header>

        <h1>История</h1>
        <p>Задумка по реализации языка появилась в конце 1980-х годов, а разработка его реализации
        началась в 1989 году сотрудником голландского института CWI Гвидо ван Россумом. Для 
        распределённой операционной системы Amoeba требовался расширяемый скриптовый язык, и Гвидо
        начал разрабатывать Python на досуге, позаимствовав некоторые наработки для языка ABC. В 
        феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. С самого
        начала Python проектировался как объектно-ориентированный язык.</p>

        <p>Гвидо ван Россум назвал язык в честь популярного британского комедийного телешоу 1970-х
        «Летающий цирк Монти Пайтона», поскольку автор был поклонником этого телешоу, как и многие
        другие разработчики того времени, а в самом шоу прослеживалась некая параллель с миром 
        компьютерной техники.</p>

        <p>Наличие дружелюбного, отзывчивого сообщества пользователей считается, наряду с дизайнерской
        интуицией Гвидо, одним из факторов успеха Python. Развитие языка происходит согласно чётко 
        регламентированному процессу создания, обсуждения, отбора и реализации документов PEP 
        (англ. Python Enhancement Proposal) — предложений по развитию Python.</p>
        <p>

            <img src="''' + url_for('static', filename = 'pechal.jpg') + ''' ">
        </p>

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/legend")
def legend():
    return '''
<!doctype html>
<html>
    <head>
        <title>Красов Павел Андреевич, лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename = 'lab1.css') + ''' " />
    </head>
    <body>
        <header>
            НГТУ, ФБ, лабораторная работа 1
        </header>

        <h1>Легенды</h1>
        <p>Истории о Тамамо-но-Маэ, легендарном духе-лисе, появляются в период Муромати как 
        отогизоси (прозаические повествования), а также упоминаются Ториямой Сэкиэном в Konjaku 
        Hyakki Shūi . Затем фольклор периода Эдо объединил легенду с похожими зарубежными 
        историями о духах-лисах, развращающих правителей и вызывающих хаос на их территориях.</p>

        <p>В истории, рассказанной Хокусаем , созданной в период Эдо , девятихвостая лиса впервые 
        появилась в Китае и овладела Дацзи , наложницей последнего правителя династии Шан, короля
        Чжоу . Она околдовала короля и навлекла на себя царство террора, которое привело к 
        восстанию, положившему конец династии Шан. Дух лисы бежал в Магадху Тяньчжу (древняя Индия)
        и стал леди Каё, наложницей наследного принца Бандзоку их, заставив его отрубить головы 
        тысяче мужчин. Затем он был снова побежден и бежал из страны. Та же лиса вернулась в Китай
        около 780 г. до н. э. и, как говорят, вселилась в Бао Си , наложницу царя Ю династии Чжоу.
        Она была снова изгнана человеческими военными силами.</p>

        <p>
            <img src="''' + url_for('static', filename = 'тамамо.jpg') + ''' ">
        </p>

        <footer>
            &copy; Красов Павел, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
'''

