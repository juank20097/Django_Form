# Usar una imagen base de Python
FROM python:3.12-slim

# Instala las dependencias del sistema, incluida pg_config
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalarlos
# Command: pip freeze > requirements.txt
COPY requirements.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --timeout=120 --ignore-installed -r requirements.txt

# Copiar el resto de la aplicación
COPY . /app/

# Asegúrate de que los archivos estáticos sean recogidos
RUN python manage.py collectstatic --noinput

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Configura el comando para ejecutar la aplicación con gunicorn
CMD ["gunicorn", "comite.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]