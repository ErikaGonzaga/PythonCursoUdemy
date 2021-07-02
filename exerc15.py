# Escreva um programa que abra um arquivo digitado pelo usuário e imprima seu conteúdo na tela

arquivo = open("arqv_usuario.txt")
linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())
    