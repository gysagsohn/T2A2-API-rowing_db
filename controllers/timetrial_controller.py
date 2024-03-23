from datetime import date
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.user import User
from models.team import Team
from models.membership import Membership
from models.timetrial import TimeTrial

timetrial_bp = Blueprint('timetrials', __name__, url_prefix='/timetrials')

@timetrial_bp.route('/', methods=['POST'])
@jwt_required()  # Require JWT authentication for creating time trials
def create_time_trial():
    try:
        # Extract data from the request
        data = request.json
        
        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()
        
        # Retrieve the user from the database
        user = User.query.get(current_user_id)
        
        # Check if the user exists
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        # Check if the user has a membership and is a captain
        membership = Membership.query.filter_by(user_id=current_user_id, is_captain=True).first()
        if not membership:
            return jsonify({'message': 'User is not a captain'}), 403
        
        # Check if the team exists and if the user is the captain of that team
        team_id = data.get('team_id')
        team = Team.query.get(team_id)
        if not team or team.id != membership.team_id:
            return jsonify({'message': 'Unauthorized'}), 401
        
        # Validate distance: must be a positive integer (in meters)
        distance = data.get('distance')
        if not isinstance(distance, int) or distance <= 0:
            return jsonify({'message': 'Distance must be a positive integer (in meters)'}), 400
        
        # Create a new time trial
        time_trial = TimeTrial(
            date_of_event=data['date_of_event'],
            distance=distance,
            time=data['time'],
            team_id=team_id
        )
        db.session.add(time_trial)
        db.session.commit()
        return jsonify({'message': 'Time trial created successfully'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to fetch all time trials
@timetrial_bp.route('/', methods=['GET'])
def get_all_time_trials():
    try:
        # Fetch all time trials from the database
        time_trials = TimeTrial.query.all()
        
        # Serialize the time trials
        time_trials_data = []
        for time_trial in time_trials:
            time_trials_data.append({
                'id': time_trial.id,
                'date_of_event': time_trial.date_of_event.strftime('%Y-%m-%d'),  # Format date as string
                'distance': time_trial.distance,
                'time': time_trial.time,
                'team_id': time_trial.team_id
            })
        
        return jsonify({'time_trials': time_trials_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@timetrial_bp.route('/<int:time_trial_id>', methods=['PUT'])
@jwt_required()  # Require JWT authentication for updating time trials
def update_time_trial(time_trial_id):
    try:
        # Extract data from the request
        data = request.json
        
        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()
        
        # Retrieve the time trial
        time_trial = TimeTrial.query.get(time_trial_id)
        
        # Check if the time trial exists
        if not time_trial:
            return jsonify({'error': f'Time trial with ID {time_trial_id} not found'}), 404
        
        # Retrieve the team associated with the time trial
        team = time_trial.team
        
        # Check if the current user is the captain of the team
        membership = Membership.query.filter_by(user_id=current_user_id, team_id=team.id).first()
        if not membership or not membership.is_captain:
            return jsonify({'error': 'You are not authorized to edit this time trial'}), 403
        
        # Update the time trial
        time_trial.date_of_event = data['date_of_event']
        time_trial.distance = data['distance']
        time_trial.time = data['time']
        db.session.commit()
        
        return jsonify({'message': 'Time trial updated successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@timetrial_bp.route('/<int:time_trial_id>', methods=['DELETE'])
@jwt_required()  # Require JWT authentication for deleting time trials
def delete_time_trial(time_trial_id):
    try:
        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()
        
        # Retrieve the time trial
        time_trial = TimeTrial.query.get(time_trial_id)
        
        # Check if the time trial exists
        if not time_trial:
            return jsonify({'error': f'Time trial with ID {time_trial_id} not found'}), 404
        
        # Retrieve the team associated with the time trial
        team_id = time_trial.team_id
        
        # Check if the current user is the captain of the team
        membership = Membership.query.filter_by(user_id=current_user_id, team_id=team_id, is_captain=True).first()
        if not membership:
            return jsonify({'error': 'You are not authorized to delete this time trial'}), 403
        
        # Delete the time trial
        db.session.delete(time_trial)
        db.session.commit()
        
        return jsonify({'message': 'Time trial deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500