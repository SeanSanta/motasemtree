from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_DB'] = 'data_db'

# Initialize MySQL
mysql = MySQL(app)

# http://localhost:5003/app/enter_data - the following will be our "Enter Data" page, which will use both GET and POST requests
@app.route('/app/enter_data', methods=['GET', 'POST'])
def enter_data():
    msg = ""  # Initialize the message
    if request.method == 'POST':
        data = request.form['data']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO data_table (data) VALUES (%s)", (data,))
        mysql.connection.commit()
        cursor.close()
        msg = "Data has been successfully submitted!"
    return render_template('enter_data.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True, port=5003)