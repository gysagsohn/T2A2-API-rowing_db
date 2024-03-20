from init import db, ma

class User(db.Model):
    # Table name in the database
    __tablename__ = "users"

    # Columns in the users table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)

# Define UserSchema for serialization/deserialization
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

# Create instances of UserSchema for single user and multiple users
user_schema = UserSchema(exclude=['password']) # Exclude password field from serialization
users_schema = UserSchema(many=True, exclude=['password'])  # Exclude password field from serialization