"""Import libraries."""
from flask import Flask

# TODO: install & import Flask-SQLAlchemy
# TODO: install & import Flask-Login
# TODO: install & import Flask-Admin

app = Flask(__name__)

# TODO: Finish connecting SQLAlchemy to a sqlite database
app.config["SQLALCHEMY_DATABASE_URI"]
# Secret keys are vital to session management (what login and admin use to authenticate)
# Secret keys should always be in a .env file
# .env should always be included in your .gitignore
# TODO: Set up a secret key

# Here we initialize db, admin, and login_manager.
db = SQLAlchemy(app)
admin = Admin(app)
login_manager = LoginManager(app)

# It is good practice to set a login_view
# users will be redirected to the route in login_view
# if they are not logged in and try to access a page that requires them to be logged in
# TODO: Add a login_view
login_manager.login_view = ""


#                           MODELS

# User inherits from db.Model and UserMixin
# db.Model comes from SQLAlchemy. This allows us to create a database table from a class
# UserMixin comes from Flask-Login. This gives the class additional methods:
# is_active, is_authenticated, is_anonymous, get_id
class User(db.Model, UserMixin):
    """User database model class."""

    id = db.Column(db.Integer, primary_key=True)
    # TODO: Add an email using a String
    # TODO: Add a password using a String


# TODO: Define an admin view for users


#                           ROUTES

# TODO: Create a home route

# TODO: Create a login route

# TODO: Create a secrets route which requires the user to be logged in

# TODO: Create a logout route (this route does not need a template)


if __name__ == __main__:
    app.run(debug=True)
