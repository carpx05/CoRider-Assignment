from marshmallow import Schema, fields, validate, pre_load, post_dump
from bson import ObjectId
from ..utils.password import hash_password

class ObjectIdField(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        return str(value)

    def _deserialize(self, value, attr, data):
        try:
            return ObjectId(value)
        except Exception:
            raise ValidationError('Invalid ObjectId')

class UserSchema(Schema):
    id = ObjectIdField(attribute='_id', dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @pre_load
    def hash_password(self, data, **kwargs):
        if 'password' in data:
            data['password'] = hash_password(data['password'])
        return data