from init import db, ma
from marshmallow import fields
from models.membership import MembershipSchema 
from models.timetrial import TimeTrialSchema

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100))
    date = db.Column(db.Date) # Date the team was created

    # Relationship with memberships
    memberships = db.relationship('Membership', back_populates='team')

    # Relationship with time trials
    timetrials = db.relationship('TimeTrial', back_populates='team')

class TeamSchema(ma.Schema):
    # Nested field for including memberships
    memberships = fields.List(fields.Nested(MembershipSchema))

    # Nested field for including time trial details
    timetrials = fields.Nested(TimeTrialSchema, only=['id', 'date_of_event', 'distance', 'time'])

    class Meta:
        fields = ('id', 'team_name', 'date', 'memberships', 'timetrials')

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)