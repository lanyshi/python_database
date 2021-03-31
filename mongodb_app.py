import pymongo

# Connect to database and collection
client = pymongo.MongoClient("mongodb://localhost")
db = client["my_db"]
col = db["pet"]

# Insert one document into collection
doc = {"name": "Coco", "owner": "Amanda", "species": "Cat", "sex": "F"}
x = col.insert_one(doc)
# Print the _id of the inserted doc
print(x.inserted_id)

# Insert many docs into collection
doc_list = [
    {"name": "Kiki", "owner": "Jack", "species": "Parrot", "sex": "F"},
    {"name": "Owen", "owner": "Kyle", "species": "Dog", "sex": "M"}
]
x = col.insert_many(doc_list)
# Print list of _id's of the inserted docs
print(x.inserted_ids)

# Find the first doc in the collection
print(col.find_one())

# Find all the docs in the collection
for d in col.find():
    print(d)

# Find docs based on specific value: name = Owen
for d in col.find({"name": "Owen"}, {"_id": 0}):
    print(d)

# Delete all docs based on certain values
x = col.delete_many({"name": "Coco", "species": "Cat"})
print(x.deleted_count, "documents deleted")

# Delete all docs in the collection
x = col.delete_many({})
print(x.deleted_count, "documents deleted")

# Drop the collection
col.drop()