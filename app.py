import flask
import json
import os

#Criar uma instância do Flask
from flask import Flask, request, jsonify
from flask_cors import CORS

#Criando a aplicação e habilitando o CORS
app = Flask(__name__)
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
    
#Criando rotas da API
#Retorna todos os treinos salvos
@app.route('/treinos', methods=['GET'])
def obter_treinos():
    treinos = ler_json()
    return jsonify(treinos)

#Adiciona um novo treino
@app.route('/treinos',methods=['POST'])
def adicionar_treino():
    novo_treino = request.json
    treinos = ler_json()
    treinos.append(novo_treino)
    salvar_json(treinos)
    return jsonify({"mensagem":"Treino adicionado com sucesso!"}), 201

#Remove um treino específico
@app.route('/trinos/<data>',methods=['DELETE'])
def deletar_treino(data):
    treinos = ler_json()
    treinos_filtrados = [t for t in treinos if t["data"] != data]

    if len(treinos) == len(treinos_filtrados):
        return jsonify({"erro": "Treino não encontrado!"}), 404
    
    salvar_json(treinos_filtrados)
    return jsonify({"mensagem": "Treino removido com sucesso!"})