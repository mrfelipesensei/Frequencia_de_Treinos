#Salvar os dados em um arquivo JSON
import json
import os

#Definição dos inputs
numero_datas = int(input("Quantos dias você deseja registrar? "))

#Lista para armazenar treinos
treinos = []

for _ in range(numero_datas):
    data = input("\nInsira a data do treino (DD-MM-AAAA): ")

    numero_grupos = int(input(f"Quantos grupos você exercitou em {data}? "))

    #Dicionário vazio que receberá os valores associados à exercicios(grupo_muscular,nome)
    exercicios = []

    '''É necessário que esse for fique dentro do anterior pois só faz sentido inserir os valores associados à exercicios dentro do escopo de numero de grupos'''
    for _ in range(numero_grupos):
        grupo_muscular = input("Insira o Grupo Muscular: ")
        nome = input("Insira o Nome do Exercício: ")
        exercicios.append({"grupo_muscular": grupo_muscular, "nome": nome})
        #Insere em exercícios os valores dos inputs

treino = {"data": data, "exercícios" : exercicios}
treinos.append(treino)
#Insere no dicionário treino os valores de data e seus respectivos exercícios(grupo_muscular,nome)
#Insere no dicionário treinos os valores do treino associado à data

#Nome do arquivo
arquivo_json = "treinos.json"

#Verifica se o arquivo já existe e carrega os dados
if os.path.exists(arquivo_json):
    with open(arquivo_json,"r") as file:
        try:
            dados_antigos = json.load(file)
        except json.JSONDecodeError:
            dados_antigos = []
else:
    dados_antigos = []

#Adiciona os novos treinos aos dados antigos
dados_antigos.extend(treinos)

#Salva os dados de volta no arquivo
with open(arquivo_json,"w") as file:
    json.dump(dados_antigos, file, indent=4)
    
print("\nTreinos salvos com sucesso!")