# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variable
ENV FLASK_APP=app.py

# Run the flask shell and execute commands
RUN flask shell <<EOF
from app import db
db.create_all()
exit()
EOF

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set the environment variable to ensure the app runs in production mode
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
