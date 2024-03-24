
from init import db, ma
from marshmallow import fields

class TimeTrial(db.Model):
    __tablename__ = "timetrials"

    # Columns in the timetrials table
    id = db.Column(db.Integer, primary_key=True)
    date_of_event = db.Column(db.Date, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    time = db.Column(db.String(100), nullable=False)
    
    # Foreign key to associate the time trial with a team
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)

    # Define the relationship with the Team model
    team = db.relationship('Team', back_populates='timetrials')

# Include foreign key IDs alongside nested objects
class TimeTrialSchema(ma.Schema):
    teams = fields.Nested('TeamSchema', only=['id', 'team_name'])

    # Include foreign key IDs in serialization
    class Meta:
        fields = ('id', 'date_of_event', 'distance', 'time', 'team')

timetrial_schema = TimeTrialSchema()
timetrials_schema = TimeTrialSchema(many=True)