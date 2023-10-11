from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

app = Flask(__name__)
# This line tells Flask where your static files are located
app.config['STATIC_FOLDER'] = 'static'  

# database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_DB'] = 'data_db'

# Initialize MySQL
mysql = MySQL(app)

# http://localhost:5002/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/app', methods=['GET', 'POST'])
def login():
    # Output error message:
    msg = "Error, I don't even know if this will output, but if it does pog"
    return render_template('index.html', msg='Log in to our crazy cool application!')

if __name__ == '__main__':
    app.run(debug=True, port=5002)