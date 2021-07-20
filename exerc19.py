#reduce
from functools import reduce

def soma (x,y):
    return x+y

lista = [1,5,60]

soma = reduce(soma,lista)
print(soma)