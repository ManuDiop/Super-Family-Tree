# Description: Dockerfile for the superfamilytree project

# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container working directory
COPY requirements.txt /app/

# Install the required packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files into the container working directory
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the app
CMD ["gunicorn", "--workers", "3", "--timeout", "120", "--bind", "0.0.0.0:8000", "superfamilytree.wsgi:application"]