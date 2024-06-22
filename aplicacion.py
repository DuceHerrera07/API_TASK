from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de una BDD en memoria
tareas = []
id_counter = 1