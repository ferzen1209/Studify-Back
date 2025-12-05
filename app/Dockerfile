FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir "uvicorn[standard]" && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Comando para ejecutar FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips=*"]
