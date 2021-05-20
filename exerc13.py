#TRATAMENTO DE EXCEÇÕES

a = 2
b = 0

try:
    print(a/b)
except:
    print("Não é possível fazer divisão por 0")

print(a/a)