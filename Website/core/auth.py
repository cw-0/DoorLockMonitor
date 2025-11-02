from . import db, bcrypt
from flask import Blueprint, redirect, render_template, request, url_for, flash 
from flask_login import login_user, logout_user
from .forms import LoginForm 
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if (user := User.query.filter_by(username=username).first()):
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Logged In", category="success")
            return redirect(url_for("views.landing"))
        else:
            flash("Invalid Password", category="error")
            return redirect(url_for("auth.login"))
    else:
        flash("Username does not exist", category="error")
        return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():
    logout_user()
    flash("Logged Out", category="success")
    return redirect(url_for("auth.login"))

# !-- Remove USER SIGNUP. Signup Will be done on backend --!
# @auth.route("/signup", methods=["GET", "POST"])
# def signup():
#     form = SignupForm()
#     if request.method == "GET":
#         return render_template("signup.html", form=form)
#
#     email = request.form.get("email")
#     username = request.form.get("username")
#     password = request.form.get("password")
#     confirm_password = request.form.get("confirm_password")
#
#     if not email:
#         flash("Missing Email", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if not username:
#         flash("Missing Username", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if not password or not confirm_password:
#         flash("Missing Passsword", category="error")
#         return redirect(url_for("auth.signup"))
#     
#     if password != confirm_password:
#         flash("Passwords do not match", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if 5 > len(password):
#         flash("Password must be more than 5 characters", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if 50 < len(password):
#         flash("Password must be 50 characters or less", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if User.query.filter_by(email=email).first():
#         flash("Email Taken", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if User.query.filter_by(username=username).first():
#         flash("Username Taken", category="error")
#         return redirect(url_for("auth.signup"))
#
#     if form.validate_on_submit():
#         password = bcrypt.generate_password_hash(password)
#         new_user = User(
#             email=email,
#             username=username,
#             password=password
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         login_user(new_user)
#         return redirect(url_for("views.landing"))
#
#     else:
#         flash("Invalid Form", category="error")
#         return redirect(url_for("auth.signup"))
