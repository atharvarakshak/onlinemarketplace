# Use Python 3.9.19 Alpine image as base
FROM python:3.9.19-alpine

# Set environment variables for Python and pip
# Install dependencies: Django and Pillow
RUN pip install django pillow

# Set working directory in the container
WORKDIR /app

# Copy the local project directory into the container's working directory
COPY . .

# Expose port 8000 (used by Django development server)

# Command to start Django server when container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
