from flask import Flask, Response, render_template, request, json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html'), 200

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html'), 200

@app.route('/signUp', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good!!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields.</span>'})

if __name__ == "__main__":
    app.run(debug=True)
