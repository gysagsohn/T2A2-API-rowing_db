from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.team import Team
from models.membership import Membership
from models.timetrial import TimeTrial

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            name="Captain test",
            email="123456@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            gender="male",
        ),
        User(
            name="Just member",
            email="memeber1@email.com", 
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            gender="male", 
        ),
        User(
            name="Just member2",
            email="memeber2@email.com", 
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            gender="female", 
        )
    ]

    db.session.add_all(users)

    teams = [
        Team(
            team_name="Team 1",
            date=date.today(),
        ),
        Team(
            team_name="Team 2",
            date=date.today(),
        ),
        Team(
            team_name="Team 3",
            date=date.today(),
        ),
    ]

    db.session.add_all(teams)

    memberships = [
        Membership(
            is_captain=True,
            user=users[0],
            team=teams[0]
        ),
        Membership(
            user=users[1],
            team=teams[1]
        ),
        Membership(
            user=users[2],
            team=teams[1]
        ),
    ]

    db.session.add_all(memberships)

     # Seed time trials
    time_trials = [
        TimeTrial(
            date_of_event=date.today(),
            distance=2000,  # Distance in meters
            time="6:30",    # Time in HH:MM format
            team=teams[0]   # Associate time trial with Team 1
        ),
        TimeTrial(
            date_of_event=date.today(),
            distance=2000,
            time="7:00",
            team=teams[1]   # Associate time trial with Team 2
        ),
    ]

    db.session.add_all(time_trials)

    db.session.commit()

    print("Tables seeded")