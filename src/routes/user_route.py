from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime
from ..extensions import  mongo
from ..utils.password import hash_password

users_bp = Blueprint('users', __name__)

def serialize_user(user):
    if user is None:
        return None
    return {
        'id': str(user['_id']),
        'name': user['name'],
        'email': user['email'],
        'created_at': user['created_at'].isoformat() if 'created_at' in user else None,
        'updated_at': user['updated_at'].isoformat() if 'updated_at' in user else None
    }

def validate_user_data(data, partial=False):
    errors = {}
    
    if not partial or 'name' in data:
        if not data.get('name') or not isinstance(data['name'], str):
            errors['name'] = 'Name is required and must be a string'
            
    if not partial or 'email' in data:
        if not data.get('email') or not isinstance(data['email'], str):
            errors['email'] = 'Email is required and must be a string'
            
    if not partial and 'password' not in data:
        errors['password'] = 'Password is required'
    elif 'password' in data and (not data['password'] or len(data['password']) < 6):
        errors['password'] = 'Password must be at least 6 characters long'
            
    return errors

@users_bp.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({'message': 'User service is running'}), 200

@users_bp.route('', methods=['GET'])
def get_users():
    users_collection = mongo.get_collection('users')
    users = list(users_collection.find())
    return jsonify([serialize_user(user) for user in users]), 200

@users_bp.route('/<id>', methods=['GET'])
def get_user(id):
    users_collection = mongo.get_collection('users')
    try:
        user = users_collection.find_one({'_id': ObjectId(id)})
        if not user:
            return jsonify({'message': 'User not found'}), 404
        return jsonify(serialize_user(user)), 200
    except Exception:
        return jsonify({'message': 'Invalid user ID'}), 400

@users_bp.route('', methods=['POST'])
def create_user():
    users_collection = mongo.get_collection('users')
    
    data = request.get_json()
    
    errors = validate_user_data(data)
    if errors:
        return jsonify({'message': 'Validation error', 'errors': errors}), 400

    existing_user = users_collection.find_one({'email': data['email']})
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 409

    user = {
        'name': data['name'],
        'email': data['email'],
        'password': hash_password(data['password']),
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow()
    }

    result = users_collection.insert_one(user)
    new_user = users_collection.find_one({'_id': result.inserted_id})
    
    return jsonify(serialize_user(new_user)), 201

@users_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    users_collection = mongo.get_collection('users')
    
    try:
        data = request.get_json()
        
        errors = validate_user_data(data, partial=True)
        if errors:
            return jsonify({'message': 'Validation error', 'errors': errors}), 400

        if 'email' in data:
            existing_user = users_collection.find_one({'email': data['email']})
            if existing_user and str(existing_user['_id']) != id:
                return jsonify({'message': 'Email already exists'}), 409

        update_data = {k: v for k, v in data.items() if k != 'password'}
        if 'password' in data:
            update_data['password'] = hash_password(data['password'])
        update_data['updated_at'] = datetime.utcnow()

        result = users_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': update_data}
        )

        if result.matched_count == 0:
            return jsonify({'message': 'User not found'}), 404
        updated_user = users_collection.find_one({'_id': ObjectId(id)})
        return jsonify(serialize_user(updated_user)), 200
    except Exception:
        return jsonify({'message': 'Invalid user ID'}), 400

@users_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    users_collection = mongo.get_collection('users')
    try:
        result = users_collection.delete_one({'_id': ObjectId(id)})

        if result.deleted_count == 0:
            return jsonify({'message': 'User not found'}), 404
        return '', 204
    
    except Exception:
        return jsonify({'message': 'Invalid user ID'}), 400
