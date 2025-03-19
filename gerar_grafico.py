import json
import os
import matplotlib.pyplot as plt
import datetime
from collections import Counter

#Nome do arquivo
arquivo_json = "treinos.json"

#Verifica se o arquivo existe
if not os.path.exists(arquivo_json):
    print("Nenhum dado encontrado.")
    exit()

#Carrega os dados
with open(arquivo_json,"r") as file:
    try:
        treinos = json.load(file)
    except json.JSONDecodeError:
        print("Erro ao carregar os dados")
        exit()

#Extrai as datas e converte para objetos datetime
datas = [datetime.datetime.strptime(treino["data"],"%d-%m-%Y") for treino in treinos]

#Conta quantos treinos por mês
datas_formatadas = [data.strftime("%Y-%m") for data in datas]
frequencia_mensal = Counter(datas_formatadas)

#Ordena dados por mês
meses = sorted(frequencia_mensal.keys())
valores = [frequencia_mensal[mes] for mes in meses]

#Calcula média de frequência
media_frequendia = sum(valores) / len(valores)

#Plota o gráfico
plt.figure(figsize=(10,5))
plt.bar(meses, valores, color='skyblue', label='Treinos no mês')
plt.axhline(media_frequendia, color='red',linestyle='dashed',label=f'Média: {media_frequendia:.1f} treinos/mês')
plt.xlabel("Mês")
plt.ylabel("Número de Treinos")
plt.title("Frequência de Treinos por Mês")
plt.legend()
plt.xticks(rotation=45)
plt.show()