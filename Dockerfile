# UPDATED Dockerfile - No LaTeX Installation Needed!
# Build time: 30 seconds instead of 5 minutes
# Image size: 200MB instead of 2GB

FROM python:3.11-slim

# Only install basic system dependencies
# NO LaTeX packages needed because we use LaTeX.Online API!
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (for better Docker caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Create temporary directories for the bot
RUN mkdir -p temp_images temp_graphs temp_pdfs output_pdfs

# Run the bot
CMD ["python", "bot.py"]
