#zip

lista1 = [1,2,3,4]
lista2 = ["objeto", "animal", "pessoa", "transporte"]
lista3 = ["faca", "cavalo", "erika", "moto"]

for numero, tipo, nome in zip(lista1,lista2,lista3):
    print(numero,tipo,nome)