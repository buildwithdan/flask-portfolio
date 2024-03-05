# Use the official Python image as the base image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Start the application
CMD ["flask", "--app", "api.index", "run", "--host=0.0.0.0", "--port=6000"]
