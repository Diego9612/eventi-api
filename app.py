import os  # para leer variables de entorno (APP_VERSION)

from flask import Flask, jsonify  # Flask = la app web; jsonify = respuesta en JSON

app = Flask(__name__)                        # crea la app; gunicorn la buscará por este nombre "app"
EVENTI = [{"id": 1, "titolo": "Jazz in Rocca"}]   # datos falsos en memoria (en ES06 vendrán de PostgreSQL)

@app.get("/health")                          # GET /health → ¿la app está viva?
def health():
    return jsonify(status="ok")              # responde {"status": "ok"}; lo usará el HEALTHCHECK en v4

@app.get("/version")                         # GET /version → qué versión está corriendo
def version():
    return jsonify(version=os.environ.get("APP_VERSION", "dev"))  # lee APP_VERSION; si no existe, "dev"

@app.get("/eventi")                          # GET /eventi → lista de eventos
def eventi():
    return jsonify(EVENTI)

if __name__ == "__main__":                   # solo si se lanza con "python app.py" (nuestro CMD)
    app.run(host="0.0.0.0", port=5000)                       # arranca en el puerto 5000