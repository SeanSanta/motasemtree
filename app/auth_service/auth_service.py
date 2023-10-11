from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
# This line tells Flask where your static files are located
app.config['STATIC_FOLDER'] = 'static'  

users = {
    "SigmaMale": "password",
    "BetaMale": "secret"
}

# http://localhost:5002/app/auth - the following will be our login page, which will use POST requests
@app.route('/app/auth', methods=['GET','POST'])

def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = request.form['username']
            password = request.form['password']
        else:
            username = request.form['username']
            password = request.form['password']

        # Check if the entered username exists in the dictionary
        if username in users:
            if users[username] == password:
                response = {'message': 'Login successful!'}
                return jsonify(response), 200
            else:
                response = {'message': 'Login failed.'}
                return jsonify(response), 401
        else:
            response = {'message': 'Username not found'}
            return jsonify(response), 404
    
    elif request.method == 'GET':
        return render_template('index.html')

    return "This route is intended for POST requests only.", 400

def home():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=5002)