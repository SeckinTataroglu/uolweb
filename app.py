from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/buttons")
def buttons():
    return render_template("buttons.html")