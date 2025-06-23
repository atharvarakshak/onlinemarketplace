# Use Python 3.9.19 Alpine image as base
FROM python:3.9.19-alpine


RUN pip install django pillow

# Set working directory in the container
WORKDIR /app


COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
