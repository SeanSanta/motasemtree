from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

app = Flask(__name__)
# This line tells Flask where your static files are located
app.config['STATIC_FOLDER'] = 'static'  

users = {
    "SigmaMale": "password",
    "BetaMale": "secret"
}


# http://localhost:5002/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/app', methods=['GET', 'POST'])
def login():
    # Output error message:
    msg = "Welcome, mortal."
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the entered username exists in the dictionary
        if username in users:
            if users[username] == password:
                msg = "Login successful"
            else:
                msg = "Invalid password"
        else:
            msg = "Username not found"
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True, port=5002)