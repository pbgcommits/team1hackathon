from flask import Flask, jsonify, render_template, jsonify, request, redirect, session
from flask_session import Session
from testdata import numSubjects, listOfSubjects, listOfClasses
from nav import findSubjectIndex
from timetableinfo import days_of_the_week, times_15m

# Currently not operational
# from db import db

app = Flask(__name__)

### WEBPAGE NAVIGATION ###

logged_in = False


@app.route("/")
@app.route("/index")
def index():
    if not logged_in:
        return redirect("/login")
    return render_template("index.html")


@app.route("/timetable")
def timetable():
    return render_template("timetable.html", days=days_of_the_week, times=times_15m, classes=listOfClasses)


@app.route("/subjects")
def subjects():
    return render_template("subjects.html", numSubjects=numSubjects, subjects=listOfSubjects)


@app.route("/subject/<subjectName>")
def subject(subjectName):
    subjectIndex = findSubjectIndex(listOfSubjects, numSubjects, subjectName)
    return render_template("subject.html", subject=listOfSubjects[subjectIndex])


@app.route("/subject/<subjectName>/assignments")
def assignment(subjectName):
    subjectIndex = findSubjectIndex(listOfSubjects, numSubjects, subjectName)
    return render_template("assignments.html", subject=listOfSubjects[subjectIndex])


@app.route("/subject/<subjectName>/grades")
def grades(subjectName):
    subjectIndex = findSubjectIndex(listOfSubjects, numSubjects, subjectName)
    return render_template("grades.html", subject=listOfSubjects[subjectIndex])


@app.route("/subject/<subjectName>/teachers")
def teachers(subjectName):
    subjectIndex = findSubjectIndex(listOfSubjects, numSubjects, subjectName)
    return render_template("teachers.html", subject=listOfSubjects[subjectIndex])


# Nobody is pretending this is secure
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html", error=None)
    else:
        for requirement in ["username", "password"]:
            if not request.form.get(requirement):
                return render_template("login.html", error=requirement)
        global logged_in
        logged_in = True
        return redirect("/")

### DATABASE LOGIC ###

# Currently not operational

# # Part 4: HTTP Post method - API to insert one recipe into the database
# @app.route("/insert-one", methods=["POST"])
# def insert_one():
#     input_json = request.get_json()

#     if db and db.collection:
#         # 進行插入操作
#         inserted_data = db.collection.insert_one(input_json)
#         # 取得插入後的 _id
#         inserted_id = str(inserted_data.inserted_id)
#         input_json["_id"] = inserted_id
#         return input_json
#     else:
#         return "Error: Unable to connect to the database or collection is not set up properly"
    

# # Part 2: Test API - Insert hard-coded data to test connection to database
# @app.route("/test")
# def test():
#     db.collection.insert_one({"name": "CISSA"})
#     return "Connected to the database!"


# # Part 3: HTTP Get method - API to return all recipes currently stored in the database
# @app.route("/get-all")
# def get_all():
#     # Collect all the data from the database
#     all = db.collection.find()

#     # For each document, convert _id from type ObjectId to string so it can be JSON serializable
#     data = []
#     for doc in all:
#         doc["_id"] = str(doc["_id"])
#         data.append(doc)

#     # Return as JSON type
#     return jsonify(data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
