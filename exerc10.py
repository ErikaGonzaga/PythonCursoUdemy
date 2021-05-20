#Arquivos

#LENDO ARQUIVO 
#arquivo = open("arquivo.txt")
# linhas = arquivo.readlines()
# print(linhas)

# for linha in linhas:
#     print(linha)

# texto_completo = arquivo.read()
# print(texto_completo)

#CRIANDO ARQUIVO
# arquivo2 = open("arquivo2.txt", "w")
# arquivo2.write("Este e o meu segundo arquivo")

# arquivo2.close()

#ALTERANDO ARQUIVO
arquivo = open("arquivo.txt","a")
arquivo.write("\nAlterando o arquivo")
arquivo.close()
