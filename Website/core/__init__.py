from dotenv import load_dotenv
from flask import Flask, redirect, url_for, flash
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_moment import Moment 
from os import getenv

load_dotenv()
APP_SECRET_KEY = getenv("FLASK_SECRET_KEY")

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
socketio = SocketIO()

def redirect_unauthorized(message="Must be logged in."):
    flash(message, category="error")
    return redirect(url_for("auth.login"))

def create_app():
    app = Flask(__name__)
    app.secret_key = APP_SECRET_KEY

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)


    migrate = Migrate(app, db)
    moment = Moment(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect_unauthorized()

    @app.errorhandler(404)
    def page_not_found(error):
        return redirect_unauthorized(message="Page Not Found")
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    socketio.init_app(app)

    return app
    
