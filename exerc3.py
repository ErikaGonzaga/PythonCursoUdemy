#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

idade = int(input("Informe sua idade: "))

if idade < 1:
    print("Não é um valor válido")
elif idade >= 18:
    print("O usuário é maior de idade")
else:
    print("O usuário é menor de idade.")