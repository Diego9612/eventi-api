# Imagen base: Linyx con Python 3.12 ya instalado
FROM python:3.12   

# Carpeta de trabajo dentro del contenedor (como hacer cd /app)
WORKDIR /app

# Copia todo de eventi-api (1er punto) a /app (2 punto)
COPY . .

#l CONSTRUIr la iamgen: instala las librerias de la lissta
RUN pip install -r requirements.txt

# Al ARRANCAR el contenedor: anza la API 
CMD ["python", "app.py"]