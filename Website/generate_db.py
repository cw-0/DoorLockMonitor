import os
from dotenv import load_dotenv
from core import create_app, db
from core.models import Doors, User

def initialize_defaults():
    load_dotenv()
    DEFAULT_USER_PASS = os.getenv("DEFAULT_USER_PASS")
    if not DEFAULT_USER_PASS:
        raise ValueError("DEFAULT_USER_PASS not found in .env")

    app = create_app()
    with app.app_context():
        if not User.query.filter_by(username="Test").first():
            admin = User(username="Test", email="Test@gmail.com", password=DEFAULT_USER_PASS)
            db.session.add(admin)

        doors_data = [
            {"doorname": "Front Door", "status": "Unknown"},
            {"doorname": "Master Bedroom Door", "status": "Unknown"},
            {"doorname": "Patio Door", "status": "Unknown"},
            {"doorname": "Kitchen Door", "status": "Unknown"},
        ]

        for door_info in doors_data:
            if not Doors.query.filter_by(doorname=door_info["doorname"]).first():
                db.session.add(Doors(**door_info))
        db.session.commit()
        print("DB Generated")

if __name__ == "__main__":
    initialize_defaults()
