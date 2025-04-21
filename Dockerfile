# Most of the time, Alpine is a great base image to start with.
# If we're building a container for Python, we use something different.
# Learn why here: https://pythonspeed.com/articles/base-image-python-docker-images/
# TLDR: Alpine is very slow when it comes to running Python!

# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

# Set a working directory inside the container
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
