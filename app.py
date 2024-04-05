from flask import Flask, jsonify, render_template, request
from db import db

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

# Part 4: HTTP Post method - API to insert one recipe into the database
@app.route("/insert-one", methods=["POST"])
def insert_one():
    input_json = request.get_json()

    if db and db.collection:
        # 進行插入操作
        inserted_data = db.collection.insert_one(input_json)
        # 取得插入後的 _id
        inserted_id = str(inserted_data.inserted_id)
        input_json["_id"] = inserted_id
        return input_json
    else:
        return "Error: Unable to connect to the database or collection is not set up properly"
    
# Part 2: Test API - Insert hard-coded data to test connection to database
@app.route("/test")
def test():
    db.collection.insert_one({"name": "CISSA"})
    return "Connected to the database!"


# Part 3: HTTP Get method - API to return all recipes currently stored in the database
@app.route("/get-all")
def get_all():
    # Collect all the data from the database
    all = db.collection.find()

    # For each document, convert _id from type ObjectId to string so it can be JSON serializable
    data = []
    for doc in all:
        doc["_id"] = str(doc["_id"])
        data.append(doc)

    # Return as JSON type
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=8000, debug=True)