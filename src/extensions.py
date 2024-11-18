from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_cors import CORS


class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    def init_app(self, app):
        # Use connection string from config
        self.client = MongoClient(app.config['CONNECTION_STRING'], connect=False)
        
        # Extract database name from URI or use default
        db_name = app.config.get('MONGO_DBNAME', 'userdb')
        self.db = self.client[db_name]
        print("MongoDB initialized: ", self.db)
        return self.db

    def get_collection(self, collection_name):
        if self.db is None:
            raise ValueError("MongoDB not initialized. Call init_app first.")
        return self.db[collection_name]

mongo = MongoDB()
bcrypt = Bcrypt()
cors = CORS()