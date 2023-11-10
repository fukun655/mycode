# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the local code to the container's working directory
COPY dragonlanding.py /app/

# Install any dependencies
# If your script requires additional dependencies, list them in a requirements.txt file
# and copy and install them here
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt

# Command to run your Python script
CMD ["python", "dragonlanding.py"]
