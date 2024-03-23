import os #to use .env 
from flask import Flask
from init import db, ma, bcrypt, jwt # Importing necessary Flask extensions

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    app.json.sort_keys = False

    #so that our details are not posted on github
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # Initialize Flask extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.team_controller import teams_bp
    app.register_blueprint(teams_bp)

    from controllers.timetrial_controller import timetrial_bp
    app.register_blueprint(timetrial_bp)

    # Return the configured Flask application   
    return app 