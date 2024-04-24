import json
from google.cloud import firestore

# Initialized the Firestore client
db = firestore.Client(project = "chatbotdeploygcp", database = "library-data")

# Loaded data from library_data.json
with open('data/library_data.json') as json_file:
    data = json.load(json_file)
    
# Create collections and add documents
books_ref = db.collection("books")

for book in data["books"]:
    books_ref.add({
        "title": book["title"],
        "author": book["author"],
        "location": book["location"],
        "availability": book["availability"]
    }) 
    
# Created a collection for library_hours and add document
db.collection("library_hours").add({"hours": data["library_hours"]})

# Created a collection for library_policies and add document
db.collection("library_policies").add({"policies": data["library_policies"]})

# Created a collection for library_events and add document 
db.collection("library_events").add({"events":data["library_events"]})


    