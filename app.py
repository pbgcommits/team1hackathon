from flask import Flask, render_template, jsonify, request
from bson import ObjectId

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# Test data
numSubjects = 4
listOfSubjects = []
tmpImageURI = "img/unimelblogo.png"
for i in range(1, numSubjects + 1):
    subject = "Subject " + str(i)
    listOfSubjects.append({
        "name": subject, 
        "code": "COMP1000" + str(i), 
        "teachingPeriod": {
            "year": 2024, "semester": 1
            },
        "imgURI": tmpImageURI
        })

@app.route("/subjects")
def subjects():
    return render_template("subjects.html", numSubjects=numSubjects, subjects=listOfSubjects)

@app.route("/timetable")
def timetable():
    return render_template("timetable.html")

@app.route("/subject/<subjectName>")
def subject(subjectName):
    subjectIndex = -1
    for i in range(numSubjects):
        if listOfSubjects[i]["name"] == subjectName:
            subjectIndex = i
            break
    print(i)
    return render_template("subject.html", subject=listOfSubjects[i])