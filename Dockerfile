# syntax=docker/dockerfile:1

# Pull the latest version of python 3
FROM python:3

# Display output in terminal
ENV PYTHONUNBUFFERED=1

# Set docker working directory to code
WORKDIR /code

# Copy the requirements.txt file into the code working directory
COPY requirements.txt /code/

# Install all packages from the requirements file
RUN pip install -r requirements.txt

# Copy the remainder of the code
COPY . /code/
