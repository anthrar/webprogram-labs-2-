from flask import Blueprint, render_template 
from flask import Blueprint, redirect, url_for, render_template, request, session, current_app
import psycopg2
lab6 = Blueprint('lab6', __name__ ) 

offices = []
for i in range(1, 11):
    if i == 5:
        offices.append({"number": i, "tenant": "Админ"})
    else:
        offices.append({"number": i, "tenant": ""})



@lab6.route('/lab6/') 
def main(): 
        return render_template('lab6/lab6.html') 


@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    if data['method'] == 'info':
        return {
            'jsonrpc': '2.0', 
            'result': offices,
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
