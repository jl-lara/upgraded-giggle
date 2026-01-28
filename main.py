from flask import Flask, render_template, request, jsonify
import time 

app = Flask(__name__)

# Base de datos en memoria (Lista de diccionarios)
puntos_guardados = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def mapa():
    return render_template('map.html')

@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    data = request.json
    lat = data.get('lat')
    lng = data.get('lng')
    
    time.sleep(1.0) # Latencia simulada para ver el spinner
    
    # Crear nombre amigable basado en el ID (Simulación de geocoding inverso)
    punto_id = len(puntos_guardados) + 1
    nombre = f"Punto de interés #{punto_id}"
    
    nuevo_punto = {
        'id': punto_id,
        'lat': lat,
        'lng': lng,
        'nombre': nombre,
        'fecha': time.strftime("%H:%M")
    }
    puntos_guardados.append(nuevo_punto)
    
    print(f"📍 Guardado: {nombre}")
    
    return jsonify({"status": "success", "punto": nuevo_punto})

# NUEVO: Endpoint para poblar la lista al iniciar
@app.route('/obtener_puntos', methods=['GET'])
def obtener_puntos():
    return jsonify(puntos_guardados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)