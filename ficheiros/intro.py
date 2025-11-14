import os

caminho = "ficheiros/dados.txt"

if os.path.exists(caminho):
	f = open(caminho,"r")
	print("Ficheiro aberto para leitura")
else:
	f=open(caminho,"w")
	print("Ficheiro criado com sucesso!")
 

# codigo para ler ou escrever no ficheiro
f.close()

with open(caminho,"w") as f:
    f.write("Primeira linha do ficheiro")
    f.write("\nSegunda linha do ficheiro")
    f.write("\nTerceira linha do ficheiro")

with open(caminho,"r") as f:
    texto = f.read()
    #texto2 = f.readline()
    #texto3 = f.readlines()
    #texto3 = [texto.strip() for texto in texto3]
    print(texto)
    #print(texto2)
    #print(texto3)
    
lista_palavras: list[str] = ["\nABC","\nDEF","\nGHI"]
with open(caminho,"a") as f:
    f.writelines(lista_palavras)
    
import csv

with open("ficheiros/produtos.csv", mode='r', newline='',encoding='utf-8') as f:
	leitor = csv.reader(f)
 
for linha in leitor:
    print(linha)