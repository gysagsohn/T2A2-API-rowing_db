from flask import Blueprint
from init import db, bcrypt
from models.user import User

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
            email="captain@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            gender="male",
            dob="1990.08.23"
        ),
        User(
            name="Just member",
            email="memeber1@email.com", 
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            gender="male", 
            dob="2000.01.01" 
        )
    ]
#need to insert error handing on this to three options
#need error handling on the way this can be inserted to DD.MM.YYYY
#see if there is a way to error handle that it is an email 

    db.session.add_all(users)
    db.session.commit()

    print("Tables seeded")