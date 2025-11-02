import bcrypt
import os
from posix import system
from dotenv import load_dotenv
from core import create_app, db
from core.models import Doors, User

def main():

    app = create_app()
    with app.app_context():
        while True:
            username = input("Username: ").strip().lower()
            clear_term()
            if username:
                if User.query.filter_by(username=username).first():
                    print("Username Taken")
                    continue
                break
            print("Missing Username")

        while True:
            email = input("Email: ").strip().lower()
            clear_term()
            if email:
                if User.query.filter_by(email=email).first():
                    print("Email Taken")
                    continue
                break
            print("Missing Email")

        while True:
            password = input("Password: ").strip()
            confirm_password = input("Confirm Password: ")
            clear_term()
            if password and confirm_password:
                if password == confirm_password:
                    if 5 <= len(password) <= 50:
                        break
                    else:
                        print("Password must be between 5 and 50 characters")
                else:
                    print("Passwords Do Not Match")
            else:
                print("Missing Password")

        bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(bytes, salt)

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        print("USER ADDED")

def clear_term():
    system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
