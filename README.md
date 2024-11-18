# CoRider-Assignment

This project is a CRUD application built with Flask, MongoDB, and Docker. It provides a RESTful API for managing users.

## Project Structure
.env.example .gitignore crud_app/ Include/ Lib/ site-packages/ pyvenv.cfg Scripts/ activate activate.bat Activate.ps1 deactivate.bat dotenv.exe flask.exe gunicorn.exe pip.exe pip3.11.exe pip3.exe python.exe pythonw.exe db_test.py docker-compose.yml Dockerfile main.py requirements.txt src/ __init__.py pycache/ .env config.py extensions.py models/ user.py routes/ pycache/ user_route.py schemas/ user.py utils/ pycache/ password.py

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:

```sh
git clone https://github.com/your-username/CoRider-Assignment.git
cd CoRider-Assignment
```

2. Create a .env file in the src directory by copying the .env.example file and updating the values.

3. Build and start the Docker containers:
```sh
docker-compose up --build
```

The API will be available at http://localhost:5000.

### API Endpoints
* GET /users/health_check - Health check endpoint
* GET /users - Get all users
* GET /users/<id> - Get a user by ID
* POST /users - Create a new user
* PUT /users/<id> - Update a user by ID
* DELETE /users/<id> - Delete a user by ID

### Project Details
#### Main Files
* main.py: Entry point of the application.
* Dockerfile: Docker configuration for the application.
* docker-compose.yml: Docker Compose configuration for the application and MongoDB.
* requirements.txt: Python dependencies.

#### Source Directory
* __init__.py: Application factory function.
* config.py: Configuration settings.
* extensions.py: Extensions initialization (MongoDB, Bcrypt, CORS).
* models/user.py: User model with CRUD operations.
* routes/user_route.py: User routes and request handlers.
* schemas/user.py: User schema definitions.
* utils/password.py: Utility functions for password hashing.
