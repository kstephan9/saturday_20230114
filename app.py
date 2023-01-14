from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello, World!"


def index():
	return render_template("index.html")
	


