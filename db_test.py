from pymongo import MongoClient

# Replace with your MongoDB connection string
connection_string = "mongodb+srv://ayushb302:SC6oy28meh4aceC5@userdb.9cjhw.mongodb.net/"
client = MongoClient(connection_string)

# Access a specific database
db = client["UserCRUD"]

# Access a specific collection
collection = db["userdb"]

# Retrieve all documents in the collection
documents = collection.find()

# Iterate through and print the documents
for doc in documents:
    print(doc)

print("Done!")
client.close()

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://ayushb302:SC6oy28meh4aceC5@userdb.9cjhw.mongodb.net/?retryWrites=true&w=majority&appName=userdb"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
