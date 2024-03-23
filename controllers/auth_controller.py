from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db, bcrypt
from models.user import User, user_schema
from models.membership import Membership, membership_schema

# Create a Blueprint for authentication endpoints
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Endpoint for user registration
@auth_bp.route("/register", methods=["POST"]) # /auth/register
def auth_register():
    try:
        # Extract data from the request body
        body_data = request.get_json()

        # Validate gender
        gender = body_data.get('gender')
        if gender not in ['male', 'female', 'non-binary']:
            return {"error": "Invalid gender. Gender must be 'male', 'female', or 'non-binary'."}, 400
        
        # Create a new user instance
        user = User(
            name=body_data.get('name'),
            email=body_data.get('email'),
            gender=gender
        )
        # Extract password from the request body and hash it
        password = body_data.get('password')
        # if password exists, hash the password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')

        # add and commit the user to DB
        db.session.add(user)
        db.session.commit()
        # Repond back to the client
        return user_schema.dump(user), 201

    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The {err.orig.diag.column_name} is required"}
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409

# Endpoint for user login to get JWT token    
@auth_bp.route("/login", methods=["POST"]) # /auth/login
def auth_login():
    # Get data from the request body
    body_data = request.get_json()
    # Find the user with the provided email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # If user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # Create a JWT token with user's ID as identity
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=5))
        
        # Retrieve user's memberships
        memberships = Membership.query.filter_by(user_id=user.id).all()
        membership_info = []
        for membership in memberships:
            membership_info.append({
                "membership_id": membership.membership_id,
                "team_name": membership.team.team_name,
                "status": membership.status,
                "is_captain": membership.is_captain
            })
        
        # Return the token along with the user info, memberships, and HTTP status code 200 (OK)
        return {
            "email": user.email,
            "token": token,
            "memberships": membership_info
        }, 200
    # else
    else:
        # Return an error response if login credentials are invalid
        return {"error": "Invalid email or password"}, 401
    
# Endpoint for user to delete their membership
# /auth/memberships/<membership_id>
@auth_bp.route("/memberships/<int:membership_id>", methods=["DELETE"]) # /auth/memberships/<membership_id>
@jwt_required()  # Require JWT authentication
def delete_membership(membership_id):
    try:
        # Get the current user's ID from the JWT token
        current_user_id = get_jwt_identity()
        
        # Retrieve the membership from the database
        membership = Membership.query.get(membership_id)
        
        # Check if the membership exists
        if not membership:
            return {"error": f"Membership with ID {membership_id} not found"}, 404
        
        # Check if the membership belongs to the current user
        if membership.user_id != current_user_id:
            return {"error": "You are not authorized to delete this membership"}, 403
        
        # Delete the membership from the database
        db.session.delete(membership)
        db.session.commit()
        
        return {"message": "Membership deleted successfully"}, 200
        
    except Exception as e:
        return {"error": str(e)}, 500
