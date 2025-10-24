# Use Python 3.11 slim base image
FROM python:3.11-slim

# Install LaTeX and dependencies for pdflatex (Springer/Nature standard)
# This is CRITICAL for perfect PDF character rendering
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-science \
    cm-super \
    dvipng \
    && rm -rf /var/lib/apt/lists/*

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
