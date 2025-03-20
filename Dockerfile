FROM python:3.9-slim

# Ustalamy katalog roboczy
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev

RUN apt-get update && apt-get install -y postgresql-client

# Kopiujemy pliki projektu
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Port, na którym działa aplikacja FastAPI
EXPOSE 8000

# Skrypt startowy - czekamy na bazę danych i uruchamiamy aplikację
CMD ["sh", "-c", "python -m app.wait_for_db && uvicorn app.main:app --host 0.0.0.0 --port 8000"]