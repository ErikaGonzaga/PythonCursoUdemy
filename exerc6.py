#realizar operações matemáticas

num1 = float(input("Digite o primeiro número "))
operador = input("Digite o operador ")
num2 = float(input("Digite o segundo número "))

# soma +
if(operador == "+"):
    resultado = num1 + num2

# subtração -
elif(operador == "-"):
    resultado = num1 - num2

# multiplicação *
elif(operador == "*"):
    resultado = num1 * num2

#divisão /
elif(operador == "/"):
    resultado = num1 / num2

# módulo %
elif(operador == "%"):
    resultado = num1 % num2

# exponenciação **
elif(operador == "**"):
    resultado = num1 ** num2

#se não for nenhuma das opções
else:
    resultado = "Operador não identificado"

print(resultado)