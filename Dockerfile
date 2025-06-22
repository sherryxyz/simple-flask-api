# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask torch torchvision pillow

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
