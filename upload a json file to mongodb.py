from pymongo import MongoClient

# if I need to upload the file
import json

# connect to database
connection = MongoClient("mongodb+srv://sviatoslavlatyk11:F3omowNLEcvi6uMn@connection0.urtg1xc.mongodb.net/?retryWrites=true&w=majority")


# creating the database -> name 'Words'
database = connection["Words"]

# creating the collection -> name 'data'
collection = database["data"]


# uploading the file to mongodb

with open('data.json') as file:
  file_data = json.load(file)

if isinstance(file_data, list):
  collection.insert_many(file_data)
else:
  collection.insert_one(file_data)


# finding a word in the database
for x in collection.find({"word": "animal"}):
  print(x)



