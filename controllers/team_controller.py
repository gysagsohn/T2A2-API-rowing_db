from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.team import Team, team_schema, teams_schema
from models.membership import Membership, membership_schema, memberships_schema


# Create a Blueprint named 'teams' with URL prefix '/teams'
teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

# Define a route to handle GET requests to '/teams/'
# http://localhost:7012/teams - GET
@teams_bp.route('/')
#to get all of the teams
def get_all_teams():
    stmt = db.select(Team).order_by(Team.date.desc())
    teams = db.session.scalars(stmt)
    return teams_schema.dump(teams)

# http://localhost:7012/teams/1 - GET
@teams_bp.route('/<int:team_id>')
#to get 1 team details
def get_one_team(team_id): 
    stmt = db.select(Team).filter_by(id=team_id)
    team = db.session.scalar(stmt)
    if team:
        return team_schema.dump(team)
    else:
        return {"error": f"Team with id {team_id} not found"}, 404
    
# Create new team
# http://localhost:7012/teams - POST
@teams_bp.route('/', methods=["POST"])
@jwt_required()
def create_team():
    body_data = request.get_json()
    creator_id = get_jwt_identity()

    # Create a new team
    team = Team(
        team_name=body_data.get('team_name'),
        date=date.today()
    )

    # Create a new membership for the creator of the team
    membership = Membership(
        status="Approved",  # Assuming the creator's membership is automatically approved
        is_captain=True,    # Assuming the creator is the captain of the team
        user_id=creator_id,
        team=team
    )

    # Add both the team and the membership to the session and commit
    db.session.add(team)
    db.session.add(membership)
    db.session.commit()

    return team_schema.dump(team), 201


# Delete team
# https://localhost:7012/teams/1 - DELETE
@teams_bp.route('/<int:team_id>', methods=["DELETE"])
@jwt_required()
def delete_team(team_id):
    # Fetch the team by its primary key
    team = Team.query.get(team_id)
    
    # Check if the team exists
    if not team:
        return {'error': f"Team with id {team_id} not found"}, 404
    
    # Get the current user's ID from the JWT token
    current_user_id = get_jwt_identity()
    
    # Check if the current user is the captain of the team
    is_captain = Membership.query.filter_by(team_id=team_id, user_id=current_user_id, is_captain=True).first()

    # If the current user is not the captain of the team, return a 403 error
    if not is_captain:
        return {'error': "You are not authorized to delete this team"}, 403
    
    # Delete all memberships associated with the team
    Membership.query.filter_by(team_id=team_id).delete()
    
    # Delete the team from the database session
    db.session.delete(team)
    
    # Commit the changes
    db.session.commit()
    
    # Return a success message
    return {'message': f"Team with id {team_id} deleted successfully"}, 200

# Update team details
# Endpoint: http://localhost:7012/teams/<team_id> - PUT, PATCH
@teams_bp.route('/<int:team_id>', methods=["PUT", "PATCH"])
def update_team(team_id):
    # Retrieve the JSON data from the request body
    body_data = request.get_json()
    # Query the database to find the team by its ID
    team = Team.query.get(team_id)
    # If the team does not exist
    if not team:
        # Return an error message indicating that the team with the specified ID was not found
        return {'error': f'Team with id {team_id} not found'}, 404
    
    # Update the team's fields with the data from the request, if provided
    if 'team_name' in body_data:
        team.team_name = body_data['team_name']
    
    # Commit the changes to the database
    db.session.commit()
    
    # Return the updated team in JSON format
    return team_schema.dump(team)
    
# Add membership to a team
# http://localhost:7012/teams/<team_id>/memberships - POST
@teams_bp.route('/<int:team_id>/memberships', methods=["POST"])
@jwt_required()
def add_membership(team_id):
    current_user_id = get_jwt_identity()
    is_captain_request = request.json.get("is_captain", False)
    # Check if the team exists
    team = Team.query.get(team_id)
    if not team:
        return {"error": f"Team with id {team_id} not found"}, 404
    
    # Check if the user is already a member of the specified team
    existing_membership = Membership.query.filter_by(user_id=current_user_id, team_id=team_id).first()
    if existing_membership:
        return {"error": "You are already a member of this team"}, 400
    
    # Check if there is already a captain for the team
    current_captain = Membership.query.filter_by(team_id=team_id, is_captain=True).first()

    if current_captain and is_captain_request:
        return {"error": "There is already a captain for this team"}, 400
    
    # Check if the team has reached the maximum number of members
    if len(team.memberships) >= 6:
        return {"error": "Maximum number of members reached for this team"}, 400
    
    # Determine if the current user is requesting to be the captain
    is_captain = is_captain_request

    # Automatically approve membership if joining as a captain
    if is_captain:
        status = "Approved"
    else:
        status = "Pending"

    # Create a new membership
    new_membership = Membership(
        status=status,
        is_captain=is_captain,
        user_id=current_user_id,
        team_id=team_id
    )
    # Add the membership to the session and commit
    db.session.add(new_membership)
    db.session.commit()
    # Get the details of the user
    user_details = {"name": new_membership.user.name, "email": new_membership.user.email}
    # Construct the response message
    response_message = {"message": "New member added to the team.",
                        "member_details": user_details,
                        "is_captain": new_membership.is_captain,
                        "status": status}

    return response_message, 201

# Approve membership request by captain
# Endpoint: http://localhost:7012/teams/<team_id>/memberships/<membership_id>/approve - PUT
@teams_bp.route('/<int:team_id>/memberships/<int:membership_id>/approve', methods=["PUT"])
@jwt_required()
def approve_membership(team_id, membership_id):
    current_user_id = get_jwt_identity()

    # Fetch the team by its ID
    team = Team.query.get(team_id)
    
    # Check if the team exists
    if not team:
        return {"error": f"Team with id {team_id} not found"}, 404

    # Check if the current user is the captain of the team
    is_captain = Membership.query.filter_by(team_id=team_id, user_id=current_user_id, is_captain=True).first()

    # If the current user is not the captain of the team, return a 403 error
    if not is_captain:
        return {"error": "You are not authorized to approve membership requests for this team"}, 403

    # Retrieve the membership by its ID
    membership = Membership.query.get(membership_id)
    
    # Check if the membership exists
    if not membership:
        return {"error": f"Membership with id {membership_id} not found"}, 404

    # Check if the membership is for the correct team
    if membership.team_id != team_id:
        return {"error": f"Membership with id {membership_id} does not belong to team {team_id}"}, 400

    # Update the membership status to "Approved"
    membership.status = "Approved"
    db.session.commit()

    # Construct the response message
    response_message = {"message": "Membership request approved successfully."}

    return response_message, 200

# Remove member from team
# Endpoint: http://localhost:7012/teams/<team_id>/members/<member_id>/remove - DELETE
@teams_bp.route('/<int:team_id>/members/<int:member_id>/remove', methods=["DELETE"])
@jwt_required()
def remove_member(team_id, member_id):
    current_user_id = get_jwt_identity()

    # Check if the current user is the captain of the team
    team = Team.query.get(team_id)
    if not team:
        return {"error": f"Team with id {team_id} not found"}, 404

    if team.user_id != current_user_id:
        return {"error": "You are not authorized to remove members from this team"}, 403

    # Check if the member belongs to the team
    membership = Membership.query.filter_by(team_id=team_id, user_id=member_id).first()
    if not membership:
        return {"error": f"User with id {member_id} is not a member of team {team_id}"}, 404

    # Delete the membership from the database
    db.session.delete(membership)
    db.session.commit()

    return {"message": "Member removed from the team successfully"}, 200
