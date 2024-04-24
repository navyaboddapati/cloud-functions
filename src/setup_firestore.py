from google.cloud import firestore

# Initialized the firestore client
db = firestore.Client(project = "chatbotdeploygcp", database = "library-data")

# Function of setup Firestore
def setup_firestore():
    
    # Creating the books collection
    books_ref = db.collection("books")
    books_data = [
                 {"title": "Book 1","author": "Author 1","location":"Shelf A", "availability": "Available"},
                 {"title" : "Book 2","author": "Author 2", "location": "Shelf B", "availability": "Checked out"}
    ]
    
    for book in books_data:
        books_ref.add(book)
        
    # Create the library_hours collection
    library_hours_ref = db.collection("library_hours")
    library_hours_data = {"hours": "Monday-Friday: 8AM - 8PM, Saturday: 10 AM - 6PM, Sunday: Closed"}
    library_hours_ref.add(library_hours_data)
    
    # Create the "library policies" collection
    library_policies_ref = db.collection("library_policies")
    library_policies_data = {"Policies": "1.No food or drink allowed in the libray. \n 2. Quite study in 4th floor and 5th floor and mut be respected \n 3. Overdue fines apply for late returns."}
    library_policies_policies_ref.add(library_policies_data)
    
    # Create the library events collection
    library_events_ref = db.collection("library_events")
    library_events_data = {"events": "Water paint on April 11th"}
    library_events_ref.add(library_events_data)
    
    if __name__ == "__main__":
        setup_firestore()
