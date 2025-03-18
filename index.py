#Definição dos inputs
data = input("Insira a data do treino: ")
grupo_muscular = input("Insira o Grupo Muscular: ")
nome = input("Insira o Nome do Exercício: ")

#Criação de um dicionário com os dados inseridos
treino = {
    "data" : data,
    "exercicios" : [{"grupo_muscular": grupo_muscular, "nome": nome}]
}

'''print(treino)'''