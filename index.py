#Salvar os dados em um arquivo JSON
import json
import os

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

#Transforma possíveis dados antigos em um dicionário para facilitar a busca por data
treinos_por_data = {treino["data"]: treino for treino in dados_antigos}

#Definição dos inputs
while True:
    try:
        numero_datas = int(input("Quantos dias você deseja registrar? "))
        if numero_datas <= 0:
            print("Insira um número mairo que zero")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

#Lista para armazenar treinos novos
treinos_novos = []

for _ in range(numero_datas):
    data = input("\nInsira a data do treino (DD-MM-AAAA): ")

    #Verifica se a data já existe nos registros
    if data in treinos_por_data:
        escolha = input(f"A data {data} já possui treinos registrados. Deseja sobrescrever? (S/N): ").strip().lower()
        if escolha == "s":
            print(f"Substituindo o treino de {data}.")
        else:
            print(f"Treino do dia {data} mantido.\n")
            continue #Pula para a próxima iteração, mantendo os dados antigos

    numero_grupos = int(input(f"Quantos grupos você exercitou em {data}? "))

    #Dicionário vazio que receberá os valores associados à exercicios(grupo_muscular,nome)
    exercicios = []

    '''É necessário que esse for fique dentro do anterior pois só faz sentido inserir os valores associados à exercicios dentro do escopo de numero de grupos'''
    for _ in range(numero_grupos):
        grupo_muscular = input("Insira o Grupo Muscular: ")
        nome = input("Insira o Nome do Exercício: ")
        exercicios.append({"grupo_muscular": grupo_muscular, "nome": nome})
        #Insere em exercícios os valores dos inputs

    #Adiciona o treino do dia à lista de treinos
    treino = {"data": data, "exercícios" : exercicios}
    treinos_novos.append(treino)
    #Insere no dicionário treino os valores de data e seus respectivos exercícios(grupo_muscular,nome)
    #Insere no dicionário treinos os valores do treino associado à data

#Atualiza os dados antigos com os novos treinos
for treino_novo in treinos_novos:
    treinos_por_data[treino_novo["data"]] = treino_novo

#Converte de volta para lista para salvar no JSON
dados_atualizados = list(treinos_por_data.values())

#Salva os dados de volta no arquivo
with open(arquivo_json,"w") as file:
    json.dump(dados_atualizados, file, indent=4)
    
print("\nTreinos salvos com sucesso!")