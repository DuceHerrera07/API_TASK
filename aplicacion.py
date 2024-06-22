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

#En listar una tarea por identificador GET
@app.route('/tareas/<int:tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea:
        return jsonify(tarea), 200
    return jsonify({'mensaje': 'Tarea no encontrada'}), 404

#DELETE
@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [tarea for tarea in tareas if tarea['id'] != tarea_id]
    return jsonify({'mensaje': 'La tarea se elimino con éxito!'}), 200

#PUT
@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def modificar_tarea(tarea_id):
    data = request.get_json()
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea:
        tarea['descripcion'] = data.get('descripcion', tarea['descripcion'])
        tarea['fecha_maxima'] = data.get('fecha_maxima', tarea['fecha_maxima'])
        return jsonify(tarea), 200
    return jsonify({'mensaje': 'La tarea no se podido encontrar.'}), 404