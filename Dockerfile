# FIXED Dockerfile - Minimal LaTeX (WORKS!)
# Build time: 2-3 minutes
# Image size: ~800MB (much better than 2GB!)

FROM python:3.11-slim

# Install ONLY essential LaTeX packages (minimal but working)
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-latex-extra \
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
