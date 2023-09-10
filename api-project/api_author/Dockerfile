FROM python:latest

# Set the working directory
WORKDIR /author_api

# Copy the requirements file and other necessary files
COPY ./requirements.txt /author_api/requirements.txt
COPY ../labrary_books.json /author_api/labrary_books.json
COPY ./author_api.py /author_api/author_api.py

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /author_api/requirements.txt

# Expose the port that your FastAPI application will run on
EXPOSE 8080

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "author_api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
