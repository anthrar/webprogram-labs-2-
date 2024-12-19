from flask import Blueprint, redirect, url_for, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab8 = Blueprint('lab8',__name__)

# routes
@lab8.route("/lab8/")
def lab():
    return render_template('lab8/lab8.html')
