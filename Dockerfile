# Etapa runtime
FROM python:3.11-slim

# Evitar buffers y bytecode
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crear directorio
WORKDIR /app

# Instalar dependencias del sistema mínimas
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto de Gunicorn
EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "wsgi:app", "--workers", "2", "--threads", "4", "--timeout", "60"]
