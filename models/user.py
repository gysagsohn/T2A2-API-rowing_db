from init import db, ma
from marshmallow import fields
from models.membership import MembershipSchema

class User(db.Model):
    # Table name in the database
    __tablename__ = "users"

    # Columns in the users table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)

    # Relationship with memberships
    memberships = db.relationship('Membership', back_populates='user', cascade='all, delete-orphan')

# Include foreign key IDs alongside nested objects
class UserSchema(ma.Schema):
    memberships = fields.List(fields.Nested(MembershipSchema))
    
    # Include foreign key IDs in serialization
    class Meta:
        fields = ('id', 'name', 'email', 'gender', 'memberships')

# Create instances of UserSchema for single user and multiple users
user_schema = UserSchema()  # No need to exclude password here, as it's not included in the model
users_schema = UserSchema(many=True)
