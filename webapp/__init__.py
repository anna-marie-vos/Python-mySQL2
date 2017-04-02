from flask import Flask, Response, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html'), 200

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html'), 200

if __name__ == "__main__":
    app.run(debug=True)
