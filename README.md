# Real-time Door Lock Monitor

A real-time dashboard system for monitoring the locked/unlocked status of doors in your house, built with Flask and IoT device integration.

## Overview

This project consists of two main components:
- **Web Dashboard**: A Flask-based web application that displays door status in real-time
- **IoT Device Code**: C++ code that runs on IoT devices attached to door locks to report their status

## Features

-  Real-time door lock status monitoring
-  WebSocket-based live updates (no page refresh needed)
-  User authentication system
-  Support for multiple doors
-  REST API for IoT device communication

### Backend
- **Flask**: Web framework
- **Flask-SocketIO**: Real-time WebSocket communication
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Flask-Bcrypt**: Password hashing
- **SQLite**: Database

### IoT Devices
- **C++**: Device-side code
- **curl**: HTTP requests to update door status
- ESP32 Dev Board w/ WiFi
- Hall Effect sensor
- TP4056
- 3.7V 1000mah LiPo Battery

## Project Structure

```
.
├── Website/
│   └── core/
│       ├── __init__.py          # App factory and configuration
│       ├── auth.py              # Authentication routes
│       ├── views.py             # Main application routes
│       ├── models.py            # Database models
│       ├── forms.py             # WTForms definitions
│       ├── static/              # CSS, JS, images
│       └── templates/           # HTML templates
└── IoT/
    ├── main.cpp                 # IoT device code
    └── config.ini               # Device configuration
```

## Database Models

### User
- `user_id`: Primary key
- `username`: Unique username (5-25 characters)
- `email`: Unique email address
- `password`: Bcrypt hashed password

### Doors
- `door_id`: Primary key
- `doorname`: Door identifier (e.g., "Front Door")
- `status`: Current status ("Locked" or "Unlocked")

### Web Routes
- `GET /` - Dashboard (requires authentication)
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /logout` - Logout user

### API Routes
- `PUT /door-status` - Update door status from IoT devices
  ```json
  {
    "doorname": "Front Door",
    "status": "Locked"
  }
  ```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cw-0/DoorLockMonitor 
   cd "DoorLockMonitor"
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```
   FLASK_SECRET_KEY=your-secret-key-here
   ```

4. **Initialize the database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   python3 app.py
   ```

## IoT Device Setup

1. **Compile the C++ code**
   ```bash
   cd IoT
   g++ main.cpp -o door_monitor
   ```

2. **Create config.ini**
   ```
   Front Door
   ```
   (Replace with appropriate door name)

3. **Run the device monitor**
   ```bash
   ./door_monitor
   ```

## Planned Features (TODOs)

From the IoT device code:
- [ ] Continuous monitoring loop
- [ ] Hall sensor integration for automatic status detection
- [ ] Smart status change detection (only send updates when status changes)
- [ ] Configurable sleep intervals between status checks
- [ ] Add battery level display per door
- [ ] Add protected requests (send door_pass with request and check on backend)

## Security Notes

- User signup is disabled by default and must be done via backend
- Passwords are hashed using bcrypt
- Login required for dashboard access
- Session management via Flask-Login

## Configuration

The Flask app uses the following configuration:
- **Database**: SQLite (`database.db`)
- **Secret Key**: Loaded from environment variable `FLASK_SECRET_KEY`
- **Login Manager**: Handles unauthorized access redirects
