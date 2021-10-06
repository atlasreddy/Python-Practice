from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
# By default flask looks for files inside the templates folder.


@app.route("/")
def index():
    return f"Welcome !! The time is {datetime.now()}"


@app.route("/test")
def test_page():
    return "<h1>TEST route</h1>"


@app.route("/test/<string:test_arg>", methods=["GET", "POST"])
def test_arg_page(test_arg):
    if request.method == "GET":
        return f"Get request {test_arg}"
    return f"<h1>TESTING THE PAGE {test_arg}</h1>"


@app.route("/test_html")
def test_html():
    return render_template("index.html", trial_info="Trial app")


if __name__ == "__main__":
    app.run(debug=True)

# pip install flask
# python app.py
