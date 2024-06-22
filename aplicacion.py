from flask import Flask, request, jsonify

app = Flask(__name__)

#BDD en memoria
tareas = []
id_counter = 1