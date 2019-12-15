from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import datetime as dt

app = Flask(__name__)

@app.errorhandler(404)
def error404(err):
    return render_template("404.html"), 404

@app.route("/")
def hech():
    return render_template("404-hotel.html")

@app.route("/kod")
def index():
    return render_template("index.html")

app.run(host='0.0.0.0', port=80, debug=True)
