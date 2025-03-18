#Definição dos inputs

numero_datas = int(input("Quantos dias você deseja registrar? "))
numero_grupos = int(input("Quantos grupos você exercitou nesse dia? "))


data = input("Insira a data do treino: ")
grupo_muscular = input("Insira o Grupo Muscular: ")
nome = input("Insira o Nome do Exercício: ")

#Criação de um dicionário com os dados inseridos
treino = {
    "data" : data,
    "exercicios" : [{"grupo_muscular": grupo_muscular, "nome": nome}]
}

'''print(treino)'''

#Salvar os dados em um arquivo JSON
import json
import os

arquivo_json = "treinos.json"

#Verifica se o arquivo já existe e carrega os dados
if os.path.exists(arquivo_json):
    with open(arquivo_json,"r") as file:
        try:
            treinos = json.load(file)
        except json.JSONDecodeError:
            treinos = []
else:
    treinos = []

#Adiciona o novo treino à lista
treinos.append(treino)

#Salva os dados de volta no arquivo
with open(arquivo_json,"w") as file:
    json.dump(treinos, file, indent=4)
    
print("Treino salvo com sucesso.")