# Identify the most effective template for you
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Run install.sh to setup the container
RUN sh install.sh

# Make port 80 available to the world outside this container
EXPOSE 80

# Run run.sh when the container launches
CMD ["sh", "run.sh"]