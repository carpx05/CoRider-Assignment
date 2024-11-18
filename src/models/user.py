from datetime import datetime
from bson import ObjectId

class User:
    @staticmethod
    def create_user(mongo, user_data):
        user_data['created_at'] = datetime.utcnow()
        user_data['updated_at'] = datetime.utcnow()
        result = mongo.db.users.insert_one(user_data)
        return result.inserted_id

    @staticmethod
    def get_all_users(mongo):
        return list(mongo.db.users.find())

    @staticmethod
    def get_user_by_id(mongo, user_id):
        return mongo.db.users.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def get_user_by_email(mongo, email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def update_user(mongo, user_id, user_data):
        user_data['updated_at'] = datetime.utcnow()
        result = mongo.db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': user_data}
        )
        return result.modified_count > 0

    @staticmethod
    def delete_user(mongo, user_id):
        result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count > 0