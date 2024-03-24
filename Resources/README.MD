# Git Hub Repository 
https://github.com/gysagsohn/T2A2-API-rowing_db


# R1 Identification of the *problem* you are trying to solve by building this particular *app*. AND R2 Why is it a *problem* that needs solving?

The problem that I am trying to solve is based what few rowing coaches have discussed in the past. Open water rowing is a sport where organising competition and/or races between different teams is very difficult due to the logistic challenges of finding an open water that can allow for the distance, the open water having the capacity to facility multiple boats at the same time and getting all the team and equipment in one place at the time. Having a benchmark on the teams time to complete certain distance is useful in understanding the teams performance, can be a tool to motivate the team and can become a strategy in improving their performance. Also, an organisation (like a school) could have multiple teams and would want to keep a track of their performance/training with each out and this can be a simple and easy way to keep a record. 

In addition open water rowing requires few  variable, as the Olympic standard for the open weight class is 2000m, and the variables can just be is the distance and number of rowers (depending on the boat assuming an Olympic standard rowing boat). Weather condition will have an impact on performance, but it isn't considered a factor when the time or distance is considered. Therefore, a comparison on performance can easily be made on 3 different variables, distance, time and number of rowers (for this app number of rowers are not considered, that would be for version 2).

So by create a platform where rowing teams can easily sign up and keep records of different races they have done, it allows the user to use the platform to solve different challenges that they are facing. It can be used to organise races in different locations, people can use it for training and record keeping. 

# R3 Why have you chosen this database system. What are the drawbacks compared to others?

I have used Object Relational Database Management System (ORDBMS) PostgreSQL. The reason I chose this database are the following:

* Open Source and large community  - PostgrestSQL is an free open source ORDBMS that has been around since 1996 (Why Use PostgreSQL For Your Next Project? | Clean Commit 2022). It is one of the most popular database system out there and has a very large active user base (Why Use PostgreSQL For Your Next Project? | Clean Commit 2022). Meaning that there are a lot of clear examples and guidelines on the best practice on how to use it and if any problems arise, solutions on how to solved them can easily be found. In addition, there is an extensive library on PostgresSQL on how to use it and it is free to access https://www.postgresql.org/. Also, as it has been around for long time and is popular, therefore there is a lot of external libraries, like SQLalchemy, Flask, Marshmallow and others to use with the database to have greater functionality (Vojak 2022).  

* ACID Compliance - ACID stands for Atomicity, Consistency, Isolation and Durability, this ensures that database transactions occur reliably and consistently, even in the face of system failures (Why Use PostgreSQL For Your Next Project? | Clean Commit 2022).

* Structured Query Language (SQL) - PostgrestSQL use SQL as it language for interacting with the databases. SQL is a proven language with large feature for managing data, updating, query and allows an easier use with the database (Why Use PostgreSQL For Your Next Project? | Clean Commit 2022).

There are some drawbacks with the database. They are:

* Schema Rigidity - A schema in PostgreSQL represents a set of organized data structures. It serves as a container for tables, views, functions, constraints, indexes, sequences, and other database objects (PostgreSQL Schema | PostgreSQL Tutorial n.d.). As this is a relational database it has a fixed schema, meaning that a defined structure is required for the data upfront. This isn't as flexible compared to NoSQL database and require a lot of planning before the database is made to ensure that it all works  (Vojak 2022). 

* Complexity - This isn't as much of an issue here as the App that is made only has 4 tables, however, PostgreSQL is complex to set up and configure can be complex (Vojak 2022) . In addition it requires carefully explorations of the relationship between each table, for example seeing the different relationship and keys (Vojak 2022). With a large data set, this can be a very complex process, however, with only 4 tables it is complex but manageable. 


# R4 Identify and discuss the key functionalities and benefits of an ORM

ORM stands for Object Relational Mapping (Venkat 2023). ORM is used as a connector between the database and an  programming language (Venkat 2023).  For this App the OPM that is used is SQL Alchemy and the object-oriented programming language is Python. SQL Alchemy translates/changes the python classes and commands into tables and SQL statements (SQLAlchemy ORM Tutorial for Python Developers n.d.).

Key functionalities of ORM are:
* Mapping - ORM usually automatically maps the tables in the database to the particular language it is linked to and vice versa (Parashar 2023). For example for SQL SQL Alchemy it maps the database tables to Python classes. (Parashar 2023) This reduced the requirement of manual mapping connecting database schemas and code (Parashar 2023). 
* Object-Oriented Programming  - ORM allows OOP to be able to be used in the code, as it allows database entities into the programming language. Principles such as inheritance, encapsulation and polymorphism can be used (Parashar 2023). 
* Abstraction of Database Operations - ORM allows developers not to deal directly with the database and it language but rather use a high level language like Python and Ruby, objects which inturn deals with the database tables (Parashar 2023). This simplifies the process and reduces the volume of boilerplate code required (Parashar 2023). 
* Query Generation - some ORM allows frameworks (might be required to use other libraries or extensions) for developers to build API for quires and interaction with database, rather than writing directly to the database (Parashar 2023). For example SQLAlchemy, with Marshallow and others, can create a method in which API can be used to perform CRUD function on a SQL database (Parashar 2023). 
* Schema changes - ORM provides frameworks of schema changes (What is Object-Relational Mapping (ORM) in DBMS? 2024). This can be done by provided database schema migration (What is Object-Relational Mapping (ORM) in DBMS? 2024). Developers can define changes to the database schema as code and apply these changes incrementally, making it easier to manage database schema changes over time as the application evolves (What is Object-Relational Mapping (ORM) in DBMS? 2024). This can provide a benefit to developers as this feature would allow them to scale and change the database without too much difficulty or changes to the original code(What is Object-Relational Mapping (ORM) in DBMS? 2024).

From those functionalities and others the benefits of using ORM are:
 * Simplicity and reduction in development time - As stated my mapping and the OOP, it provides the ability for developers to use a high level language (like python) to interact with the database directly (What is Object-Relational Mapping (ORM) in DBMS? 2024). Also, they are not required to write directly into the database and can use API to create some of its requirement (What is Object-Relational Mapping (ORM) in DBMS? 2024). Therefore, this make the process simpler and streamlines the development process (What is Object-Relational Mapping (ORM) in DBMS? 2024). 
 * Code readability - Another benefits of being able to code in higher level language is that the code that interacts, builds, encapsulating the database is cleaner and more readable (What is Object-Relational Mapping (ORM) in DBMS? 2024). As the connection hides the underlying database complexity and interact with it directly
 * Query Optimization - Some ORM include query optimization and those features can be automatic. SQLAlchemy do not have those features, but Snowflake would be an example that has such (Graziano 2016). With such features, it can make the whole process quicker and easier 
 * Flexibility with database - ORM can allow code to be reusable by establish a standard way for the relationship between the code and the database. The database could be changed, therefore allowing the code to be reused (What is Object-Relational Mapping (ORM) in DBMS? 2024). Also, this is a feature of ORM as well. 


# R5 Document all endpoints for your API

**End point for Auth_controller** 

User Registration
* URL: POST http://localhost:7012/auth/register
* Description: Register a new user.
* Request Body (JSON):

```json
{
  "name": string,
  "email": string,
  "gender": string,
  "password": string
}

```
* Response: 201 Created on success:
```json
{
  "id": integer,
  "name": string,
  "email": string,
  "gender": string
}
```

* Error handling response:
    * 400 Bad Request if gender is invalid.
    * 409 Conflict if email address is already in use.

User Login
* URL: POST http://localhost:7012/auth/login
* Description: Authenticate and login a user to obtain JWT token.
* Request Body:
```json
{
  "email": string,
  "password": string
}
```
* Response: 200 OK on success:
```json
{
  "email": string,
  "token": string,
  "memberships": [
    {
      "membership_id": integer,
      "team_name": string,
      "status": string,
      "is_captain": boolean
    },
    ...
  ]
}

```
* Response if the email or password is incorrect: 401 Unauthorized if email or password is incorrect.

Delete Membership
* URL: DELETE http://localhost:7012/auth/memberships/<membership_id>
* Description: Delete a user's membership.
* Required Permissions: User must be authenticated.
* Response: 200 OK on success:

```json
{
  "message": "Membership deleted successfully"
}
```
* Response for some errors: 
    * 403 Forbidden if the membership does not belong to the current user.
    * 404 Not Found if membership not found.
    * 500 Internal Server Error if an error occurs.

**End point for team_controller** 
Get All Teams
* URL: GET http://localhost:7012/teams
* Description: Retrieve all teams.
* Response:
* 200 OK on success:
```json
[
  {
    "id": integer,
    "team_name": string,
    "date": "YYYY-MM-DD"
  },
  ...
]
```

Get One Team
* URL: GET http://localhost:7012/teams/<team_id>
* Description: Retrieve details of a specific team.
* Response: 200 OK on success:

````json
{
  "id": integer,
  "team_name": string,
  "date": "YYYY-MM-DD"
}
````
404 Not Found if team not found.

Create New Team
* URL: POST http://localhost:7012/teams
* Description: Create a new team.
* JWT Token Required: Yes
* Request Body:

```json
{
  "team_name": string
}
```
Response: 201 Created on success:
```json
{
  "id": integer,
  "team_name": string,
  "date": "YYYY-MM-DD"
}
```

Delete Team

* URL: DELETE http://localhost:7012/teams/<team_id>
* Description: Delete a team.
* JWT Token Required: Yes
* Response: 200 OK on success:
```json
{
  "message": "Team with id <team_id> deleted successfully"
}
```
* Response for error handling: 
    * 403 Forbidden if the current user is not the captain of the team.
    * 404 Not Found if team not found.

Update Team Details

* URL: PUT or PATCH http://localhost:7012/teams/<team_id>
* Description: Update details of a team.
* JWT Token Required: Yes
* Request Body:
```json
{
  "team_name": string
}
```
* Response: 200 OK on success:
```json
{
  "id": integer,
  "team_name": string,
  "date": "YYYY-MM-DD"
}
```
* Response error handling if wrong team is entere:
    * 404 Not Found if team not found.

Add Membership to Team

* URL: POST http://localhost:7012/teams/<team_id>/memberships
* Description: Add a membership to a team.
* JWT Token Required: Yes
* Request Body:
```json
{
  "is_captain": boolean
}
```
* Response: 201 Created on success:


```json
{
  "message": "New member added to the team.",
  "member_details": {
    "name": string,
    "email": string
  },
  "is_captain": boolean,
  "status": string
}
```
* Response: error handling:
    * 400 Bad Request if the team has reached the maximum number of members or if there is already a captain for the team.
    * 404 if team or member not found

Approve Membership Request

* URL: PUT http://localhost:7012/teams/<team_id>/memberships/<membership_id>/approve
* Description: Approve a membership request by the captain of the team.
* JWT Token Required: Yes
* Response: 200 OK on success:

```json
{
  "message": "Membership request approved successfully."
}
```
* Response: error:
    * 403 Forbidden if the current user is not the captain of the team.
    * 404 Not Found if team or membership not found.

Remove Member from Team

* URL: DELETE http://localhost:7012/teams/<team_id>/members/<member_id>/remove
* Description: Remove a member from the team.
* JWT Token Required: Yes
* Response: 200 OK on success:

```json
{
  "message": "Member removed from the team successfully"
}
```
* Response: error:
    * 403 Forbidden if the current user is not the captain of the team.
    * 404 Not Found if team or membership not found.

**End point for timetrial_controller** 

Create Time Trial

* URL: POST http://localhost:7012/timetrials/
* Description: Create a new time trial.
* JWT Token Required: Yes
* Request Body:
```json
{
  "date_of_event": "YYYY-MM-DD",
  "distance": integer,
  "time": string,
  "team_id": integer
}
```
* Response: 201 Created on success:
```json
{
  "message": "Time trial created successfully"
}
```
* Response: error:
    * 400 Bad Request if distance is not a positive integer.
    * 401 Unauthorized if the user is not a captain or if the team ID does not match the user's team.
    * 404 Not Found if user not found or team not found.

Get All Time Trials

* URL: GET http://localhost:7012/timetrials/
* Description: Fetch all time trials.
* JWT Token Required: No
* Response: 200 OK on success:

```json
{
  "time_trials": [
    {
      "id": integer,
      "date_of_event": "YYYY-MM-DD",
      "distance": integer,
      "time": string,
      "team_id": integer
    },
    ...
  ]
}
```
Update Time Trial

* URL: PUT http://localhost:7012/timetrials/<time_trial_id>
* Description: Update an existing time trial.
* JWT Token Required: Yes
* Request Body:
```json
{
  "date_of_event": "YYYY-MM-DD",
  "distance": integer,
  "time": string
}
```

Response: 200 OK on success:
```json
{
  "message": "Time trial updated successfully"
}
```

* Response: error handling:
    * 400 Bad Request if distance is not a positive integer.
    * 401 Unauthorized if the user is not the captain of the team associated with the time trial.
    * 404 Not Found if time trial not found.


Delete Time Trial

* URL: DELETE http://localhost:7012/timetrials/<time_trial_id>
* Description: Delete an existing time trial.
* JWT Token Required: Yes
* Response: 200 OK on success:

```json
{
  "message": "Time trial deleted successfully"
}
```
* Response: error handling:
    * 401 Unauthorized if the user is not the captain of the team associated with the time trial.
    * 404 Not Found if time trial not found.



# R6 An ERD for your app

![alt text](Resources/ERD/ERD_V3.png)

There is 4 tables
- User
- Membership (joiner table) for user and team
- Team 
- Time_Trial

* User to Membership is zero to many, as user doesn't need to have a membership. Users can have as many membership as they like, but there must be at least 1 user to a membership. This is represented in the above diagram with the crow fee notation 
* Membership table is a joiner for user to team
* Membership to team is many to one. A team must have at least 1 member, but a member can have many memberships to different teams.
* Team to Time_Trial is a zero to many relationship, as a team doesn't need to have a trial trial record, but they can have many time trial records. But at least 1 time trial must be related to a team 


# R7 Detail any third party services that your *app* will use

Please see below for all third party services that my app will use:

* SQLAlchemy - as discussed above this is an ORM. It provides a comprehensive set of tools for working with databases in Python, including ORM, schema management, query building, and database migration. This lets me interact with the database (SQLAlchemy 2018). 

* Psycopg- is a PostgreSQL database adapter for Python. It allows the application to connect to and interact with a PostgreSQL database (Gregorio n.d.) This would be at the top of my "main.py" app

* Flask - multiple library from flask is used in the app. Flask is micro web framework that is written in python and provides features and tools for building web application in Python (Wikipedia Contributors 2019).
    * Flask-SQLAlchemy - Extension of the Flask library where it adds the support feature of SQLalchemy. It provides a high level interface for interacting with databases for using Python objects (Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (3.1.x) n.d.)

    * Flask-Marshmallow - Another extension of the Flask library. This is used for serialization and deserialization of data types especially for SQLAlchemy models. It covers database objects to Python and the other way as well (Flask-Marshmallow: Flask + marshmallow for beautiful APIs — Flask-Marshmallow 0.14.0 documentation n.d.).  

    * Flask-Bcrypt - Another extension of the Flask library. This is for password hashing. Password hashing is the process in which a password or any data is changed into strings of numbers and/or letters using an algorithm. This can be used to increase security and can be used to encrypt password and checking them. Will be used when user logins into the service and used to verify their access depending on the users action. 

    * Flask-JWT-Extended -  Another extension of the Flask library .is JSON Web Token Authentication. Ths allows the creating, verification and verification of a JWT token for a user. It can be used to authenticate and authorize access in the Flask application (Flask-JWT-Extended’s Documentation — flask-jwt-extended 4.4.4 documentation n.d.). This would work in with Flask-Bcrypt (Flask-JWT-Extended’s Documentation — flask-jwt-extended 4.4.4 documentation n.d.).

* Marshmallow - A library that is in Python for object serialization and deserialization. It is a method to covert complex data types to and form JSON (and others) (marshmallow: simplified object serialization — marshmallow 3.17.1 documentation n.d.)
    * Marshmallow-SQLAlchemy - Extension of the Marshmallow library so that Marshallow and SQLAlchemy can interacting with each other. It allows for the serialization and deserializationof SQLAlchemy models using Marshmallow schemas (marshmallow-sqlalchemy — marshmallow-sqlalchemy 0.29.0 documentation n.d.)

* datetime - This is not a third party service as this is part of the Python Standard Library. It allows module for working with dates and time (Python Software Foundation 2002). Classes and function for making, changing, handle, configuring are provided in Python through this (Python Software Foundation 2002). This would be used as I want users to insert date of when they joined and time trial took place. 

* python-dotenv - This is not a third party service as this is part of the Python Standard Library, but this is for for managing environment variables from a .env file. It allows developers to configure application settings, such as database connection strings or secret keys, in a separate file for better organization and security. This library with OS working tother allows me to create the .enc and .flaskenv file to work. 

* os - technically not a third party services as this is part of Python Standard library, but this module is for interacting with the operating system (Python 2019). This and python-dotenv allow the .env file to be created and used (Python 2019). My environment variables have been set up at .env so that when I publish  to git hub my passwords (Python 2019).


# R8 Describe your projects *models* in terms of the relationships they have with each other

Please see below for how each of my models have relationships with each other:

* **User Model:**
    * Flask & SQLAlchemy:
        * The User model represents a user in the application. It defines columns such as name, email, password, and gender.
        * The memberships relationship connects the User model to the Membership model. This relationship is defined using SQLAlchemy's db.relationship function.
    * Marshmallow:
        * The UserSchema class is a Marshmallow schema used for serializing/deserializing User objects.
        * In the UserSchema class:
            * The memberships field is nested using fields.Nested(MembershipSchema), allowing the inclusion of membership details when serializing a user.
            * The Meta class specifies the fields to include during serialization.
            * Instances of UserSchema (user_schema and users_schema) are created for single and multiple users, respectively.


* **Membership Model:**
    * Flask & SQLAlchemy:
        * The Membership model represents the membership of a user in a team. It defines foreign keys user_id and team_id to establish relationships with the User and Team models.
    * Marshmallow:
        * The MembershipSchema class is used to serialize/deserialize Membership objects.
        * The schema is imported into other models (e.g., UserSchema and TeamSchema) to include membership details when serializing users and teams.

* **TimeTrial Model:** 
    * Flask & SQLAlchemy:
        * The TimeTrial model represents a time trial event. It includes a foreign key team_id to associate the time trial with a team.
    * Marshmallow:
        * The TimeTrialSchema class is used for serializing/deserializing TimeTrial objects.
        * It includes a nested TeamSchema to include team details when serializing time trials.

* **Team Model:**
    * Flask & SQLAlchemy:
        * The Team model represents a team in the application. It includes relationships with Membership and TimeTrial models.
    * Marshmallow:
        * The TeamSchema class is used for serializing/deserializing Team objects.
        * It includes nested schemas for memberships and time trials to include their details when serializing teams.

# R9 Discuss the database relations to be implemented in your application

Please see below for the relations to be implemented in my application: 

**ERD diagram**
![alt text](Resources/ERD/ERD_V3.png)

* User Model:
    * This model represents users in the system. Users can have multiple memberships and participate in multiple teams and time trials.
    * Relationship: One-to-Many with Membership (One user can have many memberships)


* Membership Model:
    * This model represents the membership of a user in a team. It serves as a joiner between users and teams, capturing additional attributes such as whether the user is a captain of the team.
    * Primary Key: id (Primary key in the users table)
        * Foreign Key: user_id (Primary key of the User model serves as the foreign key in the memberships table)
    * Relationship: Many-to-One with User (Many memberships belong to one user)
    * Relationship: Many-to-One with Team (Many memberships belong to one team)

* Team Model:
    * This model represents teams in the system. Teams can have multiple members (users) and participate in multiple time trials.
    * Primary Key: membership_id (Primary key in the memberships table)
        * Foreign Keys:
            * user_id: References the id column in the users table (One-to-Many relationship with User model)
            * team_id: References the id column in the teams table (One-to-Many relationship with Team model)
    * Relationship: One-to-Many with Membership (One team can have many members)
    * Relationship: One-to-Many with TimeTrial (One team can participate in many time trials)

* TimeTrial Model:
    * This model represents time trials conducted by teams. Each time trial is associated with a specific team and captures details such as the date of the event, distance, and time taken.
    * Primary Key: id (Primary key in the timetrials table)
        * Foreign Key:
            * team_id: References the id column in the teams table (Many-to-One relationship with Team model)
    * Relationship: Many-to-One with Team (Many time trials belong to one team)

# R10 Describe the way tasks are allocated and tracked in your project

For this project, it is the intention to use Trellow to allocate taste. Based off Scrum and Agile method, each task would be broken down into each section and allocated a due date. However, as I am new to building an API app, the first process is to get the ERD approved for the project (as it is a requirement for the project) and then update the trello after I have reviewed all of the study material about SQL and API project.

Please see below for the screen shots and the board over time and its breakdown of each task. 

**Day 1**
![alt text](Resources/Trellow/Day1.png)

Created Trello board to breakdown the assignment. As per my previous experience, I have decided to review all of my study material before breaking down each part further. However, the idea and ERD has to be approved before I can start, so that will be task 1 to be completed.

**Day 2**
![alt text](<Resources/Trellow/Day 2.png>)

Came up with the idea for the assignment. Going to make an app for rowers. I remember talking to a friends husband couple of years ago who was a rowing couch how rowing is an interesting sport as open water (open weight class) competition is 2000m no matter the team size or gender, and that other variables like weather, isn't considered. Therefore, to keep a benchmark on how a team is doing compared to others it is relatively easy, as long as it is the same gender, weight class (open for this case) and team size (1,2,4,6) it can be compared with other team. From remembering this idea, I came up with the idea to do open rowing.

**Day 3**

![alt text](Resources/Trellow/day3.png)
![alt text](<Resources/Trellow/Day 2.png>)
Idea approved. Need to review all of the previous study material before breaking the activity down.

**Day 8**
![alt text](Resources/Trellow/Day8.png)

Review of study material completed.
ERD has been updated to correctly reflect the relationship I need.
![alt text](Resources/ERD_v.1.png)

It didn't reflect both sides of the relationship correct. Please see version 2 below
![alt text](Resources/ERD_v.2.png)

The to do list have been updated to reflect the different aspect of the app I will need to build and README file that will need to go with it.  Will add more task as it developes.

**Day 9**
I not have 5 days to complete this assignment. Started with working on the README file and going to create the flasken, env, main and init

![alt text](Resources/Trellow/Day9_App.png)
![alt text](Resources/Trellow/Day9_Readme.png)
![alt text](Resources/Trellow/Day9_App.png)
 
Noticed that I will need a requirement text. So made it a requirement for update the pip freeze during the project. 
![alt text](Resources/Trellow/Day9_requirement.png)

Git hub repository
Noticed that I didn't make any comment in my project management about pushing to Git hub. Therefore added it today. 
![alt text](Resources/Trellow/Day9_github.png)


# main.py

This is where the app will run. As when I run flask it would be looking for "app.py". To fix this I will make .flaskenv and link the app with main, so that it is easier for me. Also in class we changed the port to 8080. I will not select the same port, going to select 7012.

```python
    import os #to use .env 
    from flask import Flask
    from init import db, ma, bcrypt, jwt # Importing necessary Flask extensions

    def create_app():
        # Create a Flask application instance
        app = Flask(__name__)

        #so that our details are not posted on github
        app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
        app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

        # Initialize Flask extensions
        db.init_app(app)
        ma.init_app(app)
        bcrypt.init_app(app)
        jwt.init_app(app)

        # Return the configured Flask application   
        return app 

```
# flaskenv

As per python convention the app is in main.py file. However, for flask will be looking for app.py. As I don't want to command "flask --app main run", I made the following file with the code, so that it would run on "flask run"

    ```python
    FLASK_APP=main.py
    FLASK_DEBUG=1 
    FLASK_RUN_PORT=7012
    ```


# .env

My environment variables have been set here so that when I publish the code to git hub my passwords are not shared. 

    ```python
    DATABASE_URI=
    JWT_SECRET_KEY=
    ```
to link this to the main file, "import os #to use .env" was added to the main file 


# init.py

This file will hold all of the library. 

```python
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
```

Now that I have made the app and initiated the library, I will make my first model (users) and the authentication/route process.

Two new folders:
* models: for where the database will be
    * User - make this frist
    * Member - thrid 
    * Team - second
    * Time_trial - last

![alt text](Resources/Trellow/Day9_models.png)

User table

``` python
from init import db, ma

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

user_schema = UserSchema(exclude=['password']) # {}
users_schema = UserSchema(many=True, exclude=['password']) # [{}, {}, {}]
```
I might need to add the captain requirement here and make a link to Team table as zero to 1. As a user can only be a captain of 1 team. I will first try with my original method. If I can't make it happen then I will change it. 

* Controllers
    * cli_controller -  to create the DB
    * membership_controller - for membership table
    * team_controller - for team table
    * time_trial - for time_trial table
    * auth_controller - this is for logging and route. Also will need captain requirement. But will solve that last 

![alt text](Resources/Trellow/Day9_controllers.png) - remove this and take a new picture


# auth_controller

Created Auth_controller like the way we made in class as endpoint for user to be able to be created and login. 

I have had some issues with DOB and haven't worked out the solution yet. So that has been removed from the code until I work out the solution. 

For error handling I have included the following:
    * Gender - as there are different answers to this question, I wanted to limit the option alliable and make it only 3. So the code was added to test that
    * invalid login - if the login details are incorrect, provide feed back of 401
    * unique user - I do this by checking that there is no one else with the same email using UNIQUE_VIOLATION.
    * password error - as done in class this was added to ensure that there is password and correct error message is provided return {"error": f"The {err.orig.diag.column_name} is required"}

```python
from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes

from init import db, bcrypt
from models.user import User, user_schema

# Create a Blueprint for authentication endpoints
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Endpoint for user registration URL: /auth/register
@auth_bp.route("/register", methods=["POST"]) 
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

# Endpoint for user login to get JWT token URL:  /auth/login
@auth_bp.route("/login", methods=["POST"]) 
def auth_login():
    # Get data from the request body
    body_data = request.get_json()
    # Find the user with the provided email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # If user exists and password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # Create a JWT token with user's ID as identity
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # Return the token along with the user info and HTTP status code 200 (OK)
        return {"email": user.email, "token": token,}
    # else
    else:
        # Return an error response if login credentials are invalid
        return {"error": "Invalid email or password"}, 401
```

**Day 12**
As I got a bit busy I stopped updating the readme with daily updates on the code. However, I did include completion and updates on the trello board as new develops took place. Please see below:

![alt text](Resources/Trellow/Day12_API_Controllers.png)
![alt text](<Resources/Trellow/Day12_APP_flask,env, main and init.png>)
![alt text](Resources/Trellow/Day12_beforesubmission.png)

Few task are still to be completed:

![alt text](<Resources/Trellow/Git Hub.png>)
![alt text](<Resources/Trellow/Readyme task.png>)
![alt text](<Resources/Trellow/Requirement text.png>)

The above task can only be completed after the assignment has been submitted. 


# Reference List

Why Use PostgreSQL For Your Next Project? | Clean Commit 2022, cleancommit.io.

PostgreSQL Schema | PostgreSQL Tutorial n.d., hasura.io, viewed 24 March 2024, <https://hasura.io/learn/database/postgresql/core-concepts/1-postgresql-schema/#:~:text=Schema%20is%20a%20collection%20of>.

Vojak, J 2022, Exploring the pros and cons of SQL databases — MySQL, Postgres, Oracle, Microsoft SQL, and Amazon…, Medium.

Venkat, E 2023, Why SQLAlchemy should no longer be your ORM of choice for Python projects, Medium, viewed 24 March 2024, <https://eash98.medium.com/why-sqlalchemy-should-no-longer-be-your-orm-of-choice-for-python-projects-b823179fd2fb>.

SQLAlchemy ORM Tutorial for Python Developers n.d., Auth0 - Blog.

Gregorio, FD n.d., psycopg2-binary: psycopg2 - Python-PostgreSQL Database Adapter, PyPI.Day1

Wikipedia Contributors 2019, Flask (web framework), Wikipedia, Wikimedia Foundation.

Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (3.1.x) n.d., flask-sqlalchemy.palletsprojects.com.

Flask-Marshmallow: Flask + marshmallow for beautiful APIs — Flask-Marshmallow 0.14.0 documentation n.d., flask-marshmallow.readthedocs.io.

Flask-JWT-Extended’s Documentation — flask-jwt-extended 4.4.4 documentation n.d., flask-jwt-extended.readthedocs.io.

marshmallow: simplified object serialization — marshmallow 3.17.1 documentation n.d., marshmallow.readthedocs.io.

marshmallow-sqlalchemy — marshmallow-sqlalchemy 0.29.0 documentation n.d., marshmallow-sqlalchemy.readthedocs.io.

Python 2019, os — Miscellaneous operating system interfaces — Python 3.8.0 documentation, Python.org.

Python Software Foundation 2002, Datetime — Basic Date and Time Types — Python 3.7.2 Documentation, Python.org.

SQLAlchemy 2018, SQLAlchemy - The Database Toolkit for Python, Sqlalchemy.org.

Parashar, N 2023, What is Object-Relational Mapping?, Medium, viewed 24 March 2024, <https://medium.com/@niitwork0921/what-is-object-relational-mapping-38a9830d5056>.

Graziano, K 2016, Automatic Query Optimization. No Tuning! - Blog, Snowflake, viewed 24 March 2024,

What is Object-Relational Mapping (ORM) in DBMS? 2024, GeeksforGeeks.