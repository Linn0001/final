# Orchestrator Dockerfile

# Usa una imagen base de Python
FROM python:3.8

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias a la imagen
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto a la imagen
COPY . .

# Expone el puerto en el que correrá el orquestador
EXPOSE 5000

# Comando para ejecutar el orquestador
CMD ["python", "orchestrator.py"]

