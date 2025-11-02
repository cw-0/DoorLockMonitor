from . import socketio, db 
from .models import Doors
from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def landing():
    front_door = Doors.query.filter_by(doorname="Front Door").first()
    master_bedroom_door = Doors.query.filter_by(doorname="Master Bedroom Door").first()
    patio_door = Doors.query.filter_by(doorname="Patio Door").first()
    kitchen_door = Doors.query.filter_by(doorname="Kitchen Door").first()

    front_door_status = "Unknown" if not front_door else front_door.status
    master_bedroom_door_status = "Unknown" if not master_bedroom_door else master_bedroom_door.status
    patio_door_status = "Unknown" if not patio_door else patio_door.status
    kitchen_door_status = "Unknown" if not kitchen_door else kitchen_door.status
    print(front_door_status)

    return render_template(
        "index.html",
        front_door_status=front_door_status,
        master_bedroom_door_status=master_bedroom_door_status,
        patio_door_status=patio_door_status,
        kitchen_door_status=kitchen_door_status,
    )

@views.route("/door-status", methods=['PUT'])
def update_door_status():
    data = request.get_json()
    doorname = data.get("doorname")
    status = data.get('status').strip().title()

    if status != "Locked" and status != "Unlocked":
        return {'message': f"Status: '{status}' is invalid"}
    
    door = Doors.query.filter_by(doorname=doorname).first()
    if door:
        door.status = status
        db.session.commit()
    else:
        return {'message': f"Invalid Door Name - '{doorname}'"}

    socketio.emit('door_update', {'doorname': doorname, 'status': status})
    return {'message': f"{doorname} updated to {status}"}, 200
