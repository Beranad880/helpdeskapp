FROM python:3.9-slim

WORKDIR /app

# Kopírujeme requirements.txt (už je v aktuálním adresáři, ne ve složce backend/)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopírujeme zbytek aplikace
COPY . .

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]