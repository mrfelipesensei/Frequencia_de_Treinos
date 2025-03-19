import flask
import json
import os

#Criar uma instância do Flask
from flask import Flask, request, jsonify
from flask_cors import CORS

#Criando a aplicação e habilitando o CORS
app = flask(__name__)
CORS(app)

#Definindo arquivo JSON
arquivo_json = "treinos.json"

#Função para ler o JSON
def ler_json():
    if os.path.exists(arquivo_json):
        with open(arquivo_json) as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

#Função para salvar o JSON
def salvar_json(dados):
    with open(arquivo_json,"w") as file:
        json.dump(dados,file, indent=4)
    

