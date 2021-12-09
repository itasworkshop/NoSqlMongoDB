import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print(client)
db = client['test']
print(db)
collection = db['weather']
print(collection)

with open('weather.json') as f:
    file_data = json.load(f)
    print(file_data)


if isinstance(file_data, list):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

client.close()

#db.weather.find({"currently_temperature": {$gt:25}})
#> db.weather.count({"currently_temperature": {$gt:25}})
#> db.weather.find({"currently_temperature": {$gt:10}},{"currently_temperature":1,"city":1,_id:0})