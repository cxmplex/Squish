FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app

# install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8085 available
EXPOSE 8085

# Define environment variable
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8085 --config gunicorn_config.py"

# Run main.py when the container launches using gunicorn
CMD ["gunicorn", "main:app"]
