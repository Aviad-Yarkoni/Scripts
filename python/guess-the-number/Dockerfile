#use the official Python image from Docker Hub
FROM python:3.9.19-alpine3.20

#set the working directory insite the container
WORKDIR /app

#copy from the current directory contents into the contener at /app
COPY ./guess-the-number.py ./app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run guest-the-number.py when the container launches
CMD ["python", "./app/guess-the-number.py"]

