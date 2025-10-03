#1. Crie uma lista com os números pares de 1 a 10.

lista = [i for i in range(1,11) if i % 2 == 0]
print(lista)

#2. Crie uma lista com os quadrados dos números de 1 a 10.

quadrado = [i ** 2 for i in range(1,11)]
print(quadrado)

#3. Dada uma lista de palavras, crie uma nova lista que indique o tamanho de cada
#palavra.

palavras = ["Rui","Maça","Sapo"]
palavraTamanho = [len(palavra) for palavra in palavras]
print(palavraTamanho)

#4. Dada uma lista de números, crie uma lista apenas com os números maiores que 5.

lista= []
for i in range(1,11):
    lista.append(i)
maior_que_6 = [i for i in lista if i > 5]
print(maior_que_6)

#5. Crie uma lista com as letras maiúsculas de uma string. (nome = 'MarcelO ViEiRa
#amorIM')

nome = 'MarcelO ViEiRa amorIM'
letras_maiusculas = [letra for letra in nome if letra.isupper()]
print(letras_maiusculas)

#6. Dada uma lista de números, crie uma nova lista onde se o número for múltiplo de 3,
#é apresentado o dobro deste caso contrário aparece o mesmo número da lista original.

lista= []
for i in range(1,11):
    lista.append(i)
multiplos_de_3 = [1*2 if i % 3 == 0 else i for i in lista]
print(multiplos_de_3)

#7. Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam
#com a letra "A". Todos os nomes da nova lista devem aparecer em maiúsculas.

nomes = ["Ana","Rui","João","Mariana","Alice","Luana"]
nomes_A = {nome.upper() for nome in nomes if nome.startswith('A')}
print(nomes_A)

#8. Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta,
#apenas para as frutas com mais de 5 letras. Caso contrário, deve aparecer 0.

frutas = ["Pera","Banana","Maça","Melao","Melancia"]
nova_lista = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(nova_lista)