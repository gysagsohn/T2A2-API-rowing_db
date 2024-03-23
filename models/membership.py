from init import db, ma
from marshmallow import fields

class Membership(db.Model):
    __tablename__ = "memberships"

    # Membership ID, primary key
    membership_id = db.Column(db.Integer, primary_key=True)
    # Status of the membership
    status = db.Column(db.String, default="Pending")  # Default status is "Pending"
    # Field to indicate if the user is a captain of the team
    is_captain = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)

    user = db.relationship('User', back_populates='memberships')
    team = db.relationship('Team', back_populates='memberships')

    def update_status(self, new_status):
        self.status = new_status

# Membership schema for serialization/deserialization
from marshmallow import fields, Schema

class MembershipSchema(Schema):
    # Include foreign key IDs alongside nested objects
    user = fields.Nested('UserSchema', only=['name', 'email', 'gender', 'id'])
    team = fields.Nested('TeamSchema', only=['team_name', 'date', 'id',])

    class Meta:
        fields = ('membership_id', 'status', 'is_captain', 'user', 'team')

# Create instances of MembershipSchema for single membership and multiple memberships
membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many=True)