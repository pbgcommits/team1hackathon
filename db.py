from flask_pymongo import pymongo


CONNECTION_STRING = "mongodb+srv://jacklyn:ss0806449@cluster0.pip93yq.mongodb.net/?retryWrites=true&w=majority"


# Create user that sends/receives requests
client = pymongo.MongoClient(CONNECTION_STRING)


# Find or create database
db = client.get_database("flask_mongodb_recipes")


# Create a collection (JSON format dict) within the database
collection = pymongo.collection.Collection(db, "collection")

