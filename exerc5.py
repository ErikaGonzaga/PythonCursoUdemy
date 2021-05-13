#ordenar uma lista

#lista = [5,8,9,2,4]
#lista = sorted(lista)
#print(lista)

#ordenar utilizando select sort

lista = [2,6,1,23,0,3,10,15,8]

for i in range(len(lista)):
    menor = i
    
    for j in range(i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print(lista)