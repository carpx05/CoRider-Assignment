import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/userdb')
    DB_USER = os.getenv('DB_USER', 'default-user')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    CONNECTION_STRING = f"mongodb+srv://{DB_USER}:{SECRET_KEY}@userdb.9cjhw.mongodb.net/ssl=true&ssl_cert_reqs=CERT_NONE"

try:
    client = MongoClient(Config.CONNECTION_STRING, connect=False)
    client.admin.command('ping')  
    print("Connected successfully! ", client)
except Exception as e:
    print("Failed to connect:", e)