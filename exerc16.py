x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)

print("Lista1:", x)
print("Elementos da lista1 ao quadrado:",y)

# Usando list comprehension

a = [1,2,3,4,5,6]
b = [i**2 for i in a]   #[valor_a_adicionar laco]
c = [i for i in a if i%2==1]     #[valor_a_adicionar laco condicao]

print("Lista A:",a)
print("Elementos da lista A ao quadrado:",b)
print("Números primos da lista A:",c)