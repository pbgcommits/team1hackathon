from flask_pymongo import pymongo
from secret_key import CONNECTION_STRING
import pandas as pd

 
# Create user that sends/receives requests
client = pymongo.MongoClient(CONNECTION_STRING)


# Find or create database
db = client.get_database("flask_mongodb_recipes")


# Create a collection (JSON format dict) within the database
collection = pymongo.collection.Collection(db, "collection")


# 从CSV文件中读取数据
data = pd.read_csv('appendix.csv')

# 将数据转换为字典格式并插入到MongoDB集合中
data_dict = data.to_dict(orient='records')
collection.insert_many(data_dict)