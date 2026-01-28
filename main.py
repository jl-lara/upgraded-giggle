from flask import Flask, render_template, request, jsonify
import time 

app = Flask(__name__)

# Base de datos en memoria
datos_guardados = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def mapa():
    return render_template('map.html')

@app.route('/guardar_dato', methods=['POST'])
def guardar_dato():
    data = request.json
    tipo = data.get('tipo', 'punto')
    
    time.sleep(1.0) # Simular carga
    
    # CORRECCIÓN DE LÓGICA: Numeración Independiente
    # Contamos cuántos items de este mismo tipo existen ya
    conteo_tipo = len([d for d in datos_guardados if d['tipo'] == tipo]) + 1
    
    # ID único global para sistema (no visible al usuario)
    item_id = len(datos_guardados) + 1
    
    if tipo == 'ruta':
        nombre = f"EcoRuta #{conteo_tipo}" # Ej: EcoRuta #1
        nuevo_item = {
            'id': item_id,
            'tipo': 'ruta',
            'nombre': nombre,
            'origen': data.get('origen'),
            'destino': data.get('destino'),
            'distancia': data.get('distancia'),
            'fecha': time.strftime("%H:%M")
        }
    else:
        nombre = f"Punto de interés #{conteo_tipo}" # Ej: Punto de interés #1
        nuevo_item = {
            'id': item_id,
            'tipo': 'punto',
            'nombre': nombre,
            'lat': data.get('lat'),
            'lng': data.get('lng'),
            'fecha': time.strftime("%H:%M")
        }
        
    datos_guardados.append(nuevo_item)
    print(f"📍 Guardado ({tipo}): {nombre}")
    
    return jsonify({"status": "success", "item": nuevo_item})

@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    return jsonify(datos_guardados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)