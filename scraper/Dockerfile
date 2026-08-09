# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the scraping script
COPY scrape.py .

# Run the script continuously
CMD ["python", "scrape.py"]
