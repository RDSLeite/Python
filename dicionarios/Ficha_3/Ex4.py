quadrado = {num: num ** 2 for num in range(1,11)}
print(quadrado)

lista = ['Infomatica','Python','Dicionario']
palavras = {palavra: len(palavra) for palavra in lista}
print(palavras)

notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David":12, "Eva":19}
notas_superiores_15 = {aluno: nota for aluno, nota in notas.items() if nota >= 15}
print("Notas maiores ou iguais a 15:",notas_superiores_15)