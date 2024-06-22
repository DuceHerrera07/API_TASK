from flask import Flask, request, jsonify

app = Flask(__name__)

#BDD en memoria
tareas = []
id_counter = 1

#POST
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    global id_counter
    data = request.get_json()
    tarea = {
        'id': id_counter,
        'descripcion': data['descripcion'],
        'fecha_maxima': data['fecha_maxima']
    }
    tareas.append(tarea)
    id_counter += 1
    return jsonify(tarea), 201

#GET
@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(tareas), 200

