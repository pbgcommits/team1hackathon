from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/subjects")
def subjects():
    return render_template("subjects.html")

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")