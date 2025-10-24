# Use Python 3.11 slim base image
FROM python:3.11-slim

# Install LaTeX packages needed for JEE Advanced calculus PDFs
# Includes: math symbols, tables, diagrams, professional formatting
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-pictures \
    lmodern \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc/* \
    && rm -rf /usr/share/man/* \
    && rm -rf /usr/share/locale/*

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Create necessary directories
RUN mkdir -p temp_images temp_graphs

# Run the bot
CMD ["python", "bot.py"]
