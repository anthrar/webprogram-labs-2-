from flask import Blueprint, render_template 
from flask import Blueprint, redirect, url_for, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

lab6 = Blueprint('lab6', __name__ ) 

# database
DBS = '?'
def db_connect():
    global DBS
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'pavel_krasov_knowledge_base',
            user = 'pavel_krasov_knowledge_base',
            password = '777'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        DBS = '%s'
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

offices = []
def getOfficeList():
    global offices

    conn, cur = db_connect()
    cur.execute("Select * From offices order by number")
    offices = cur.fetchall()    
    db_close(conn, cur)

def updateStatus(number, tenant):
    conn, cur = db_connect()
    cur.execute("update offices set tenant=" + DBS + " where number=" + DBS + ";",
                (tenant, number))
    conn.commit()
    db_close(conn, cur)


def generateOffices():
    for i in range(1, 11):
        if i == 5:
            offices.append({"number": i, "tenant": "Админ", 'price': 500})
        else:
            offices.append({"number": i, "tenant": "", 'price': 1000})

def TotalCost():
    cost = 0
    login = session.get('login')
    if not login:
        return 0
    
    for office in offices:
        if office['tenant'] == login:
            cost += office['price']
    return cost



@lab6.route('/lab6/') 
def main(): 
        return render_template('lab6/lab6.html') 


@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    if data['method'] == 'info':
        getOfficeList()
        return {
            'jsonrpc': '2.0', 
            'result': offices,
            'cost': TotalCost(),
            'id': id
        }
    
    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0', 
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }

    if data['method'] == 'booking':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number: 
                if office['tenant'] != '':
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }

                office['tenant'] = login
                updateStatus(office_number,login)
                return {
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                }


    if data['method'] == 'cancellation':
        office_number = data['params']
        login = session.get('login')
        if not login:
            return {
                'jsonrpc': '2.0', 
                'error': {
                    'code': 1,
                    'message': 'Unauthorized'
                },
                'id': id
            }
        for office in offices:
            if office['number'] == office_number: 
                if office['tenant'] == '':
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Офис не арендован'
                        },
                        'id': id
                    }
                if office['tenant'] != login:
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 3,
                            'message': 'Офис не арендован'
                        },
                        'id': id
                    }

                office['tenant'] = ''
                updateStatus(office_number,'')
                return {
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                }


    return {
            'jsonrpc': '2.0', 
            'error': {
                'code': -32601,
                'message': 'Method not found'
            },
            'id': id
        }
