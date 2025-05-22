# Use official lightweight Python image
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Copy requirements.txt first for caching dependencies install
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# Install python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy your notebook and other files
COPY . /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]


# start commands:
# docker build -t weather-notebook:latest .
# run command:
# docker run -p 8888:8888 weather-notebook:latest

# access from EC2 link:
# http://<ec2-public-ip>:8888