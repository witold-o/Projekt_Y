FROM python:3.9-slim

# Ustalamy katalog roboczy
WORKDIR /backend

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev

RUN apt-get update && apt-get install -y postgresql-client

# Kopiujemy pliki projektu
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend

# Port, na którym działa aplikacja FastAPI
EXPOSE 8000

# Skrypt startowy - czekamy na bazę danych i uruchamiamy aplikację
CMD ["sh", "-c", "python -m backend.wait_for_db && uvicorn backend.main:app --host 0.0.0.0 --port 8000"]
