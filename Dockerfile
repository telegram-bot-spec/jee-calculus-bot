FROM python:3.11-slim

# Install LaTeX with minimal required packages (NOT texlive-full - too large!)
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-xetex \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p temp_images temp_graphs temp_pdfs output_pdfs

CMD ["python", "bot.py"]
