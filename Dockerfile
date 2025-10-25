FROM python:3.11-slim

RUN apt-get update && apt-get install -y texlive-full \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p temp_images temp_graphs temp_pdfs output_pdfs

CMD ["python", "bot.py"]
