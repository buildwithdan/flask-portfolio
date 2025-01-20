# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /flask-portfolio

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock ./

# Install dependencies using pipenv
RUN pipenv install --ignore-pipfile

# Copy the rest of the application code into the container
COPY . .

# # Expose the port your app runs on, this doesnt do anything, its just for documentation purposes.
EXPOSE 6001

# Start the application using pipenv to ensure the correct Python environment
# Run Flask in debug mode with specified app entry point

CMD ["pipenv", "run", "flask", "--debug", "--app", "api/index.py", "run", "--host=0.0.0.0", "--port=6001"]