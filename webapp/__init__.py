from flask import Flask, Response, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return Response("hello"), 200

if __name__ == "__main__":
    app.run(debug=True)
