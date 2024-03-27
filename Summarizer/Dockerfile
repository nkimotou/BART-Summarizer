# This file instructs Docker how to build the Docker Image and containerize the FastApi application

# Use Python 3.9 image to build the Docker image
FROM python:3.9-slim

# Set up Python environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the docker container in your app folder
COPY requirements.txt /app/

# Install dependencies from the requirements.txt file or specify specific dependencies to pip install
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install transformers
RUN pip install torch
RUN pip install tensorflow
RUN pip install tf-keras

# Copy contents of the directory into your app folder
COPY . /app/

# Expose port 8000 to be accessed publically
EXPOSE 8000

# Run your FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
