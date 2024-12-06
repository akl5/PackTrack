This folder contains all the files that handle data related tasks between the frontend and server/database.

Coop-Postings_routes.py
Python file that prvides the route for retrieving the co-op posts.

db_connection
Connect to MySQL. 

rest_entry.py
Setup the Flask app.

.dockerignore
Unncessary files are excluded from the Docker build.

.env.template
Reference file containing environment variables for the project to run smoothly.

backend_app.py
Serves as entry point for Flask application.

Dockerfile
File that sets up lightweight Docker container for our Python-centered application.

Uses a Base Image: Begins with a base of the official Python 3.11 slim image.
Intiailizes Working Directory: Establishes /apicode as the working directory in the container.
Installs Dependencies: Copies requirements.txt into container and installs the required Python packages with pip.
Copies Application Code: Moves all the app files into the container.
Exposes a Port: Opens port 4000 for external access, letting the app talk with the outside world.
Defines the Application Entry Point: Defines that the container needs to run backend_app.py with Python upon start.

requirements.txt