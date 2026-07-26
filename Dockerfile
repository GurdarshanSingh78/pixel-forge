# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Hugging Face Spaces routes traffic to port 7860 by default
EXPOSE 7860

# Run the database setup, then start Uvicorn on the correct port
CMD python initial_setup.py && uvicorn app.main:app --host 0.0.0.0 --port 7860