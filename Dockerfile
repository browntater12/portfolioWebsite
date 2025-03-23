# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies and Gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application
COPY . .

# Expose port 8000 (Gunicorn's default)
EXPOSE 8080

# Set production environment
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app", "--workers", "3"] 