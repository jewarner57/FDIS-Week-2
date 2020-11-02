"""Import libraries."""
from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os

# TODO: install & import Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# TODO: install & import Flask-Login
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# TODO: install & import Flask-Admin
from flask_admin import Admin, expose, BaseView


app = Flask(__name__)

# TODO: Finish connecting SQLAlchemy to a sqlite database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///./weektwologin.db'

# Secret keys are vital to session management (what login and admin use to authenticate)
# Secret keys should always be in a .env file
# .env should always be included in your .gitignore
# TODO: Set up a secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Here we initialize db, admin, and login_manager.
db = SQLAlchemy(app)
admin = Admin(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """gets the current user object"""
    return User.query.get(int(user_id))


# It is good practice to set a login_view
# users will be redirected to the route in login_view
# if they are not logged in and try to access a page that requires them to be logged in
# TODO: Add a login_view
login_manager.login_view = "login"


#                           MODELS

# User inherits from db.Model and UserMixin
# db.Model comes from SQLAlchemy. This allows us to create a database table from a class
# UserMixin comes from Flask-Login. This gives the class additional methods:
# is_active, is_authenticated, is_anonymous, get_id
class User(UserMixin, db.Model):
    """User database model class."""

    id = db.Column(db.Integer, primary_key=True)
    # TODO: Add an email using a String
    email = db.Column(db.String(120), unique=True, nullable=False)
    # TODO: Add a username using a String
    username = db.Column(db.String(80), nullable=False)
    # TODO: Add a password using a String
    password_hash = db.Column(db.String(128), nullable=False)


class AdminView(BaseView):
    def is_accessible(self):
        """get the current authentication status of the user"""
        return current_user.is_authenticated

    # can be accessed from /admin/
    @expose('/')
    def index(self):
        """show the admin page"""
        return self.render('admin.html')


admin.add_view(AdminView(name="Admin"))


#                           ROUTES

@app.route('/')
def home():
    """displays the home page"""
    return render_template("home.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """displays the signup page"""
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        hashedPass = generate_password_hash(password)

        user = User(email=email, username=username, password_hash=hashedPass)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    else:
        return render_template("signup.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    """displays a login page"""
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("Invalid Credentials")
            return render_template("login.html")

    else:
        return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    """displays a page that can only be viewed by a logged in user"""
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    """logs out the user"""
    logout_user()
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
