from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

app = Flask(__name__)

# database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_DB'] = 'data_db'

# Initialize MySQL
mysql = MySQL(app)

# http://localhost:5002/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/app/', method=['GET', 'POST'])
def login():
    # Output error message:
    msg = "Error, I don't even know if this will output, but if it does pog"
    return render_template('index.html', msg='woo')