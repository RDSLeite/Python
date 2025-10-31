notas = {
    'sergio':{'matematica':13.25, 'programacao':17.75, 'outras':[12.25,13.50,17]},
    'gonçalo':{'matematica':14.25, 'programacao':12.50,'outras':[11.25,13.50,8.25]},
    'renan':{'matematica':16.25, 'programacao':12.75,'outras':[8.25,13.50,13.25]},
    'tomas':{'matematica':8.25, 'programacao':15,'outras':[10.25,13.50,17.75]},
}

#Imprimir a nota de matematica do gonçalo
print(notas['gonçalo']['matematica'])

#Imprimir a maior nota de matematica
maior_nota = 0
for k in notas.keys():
    if notas[k]['matematica'] > maior_nota:
        maior_nota = notas[k]['matematica']
print(maior_nota)

#Imprimir a maior nota de matematica (List comprehension)
print(max([notas[k]['matematica'] for k in notas.keys()]))


#Nova nota em outras disciplinas para o Tomas
notas['tomas']['outras'].append(16.25)
print("Media das outras disciplinas do Tomas: ")
print(f"{sum(notas['tomas']['outras']) / len(notas['tomas']['outras'])}")

#Imprimir o melhor aluno
melhor_aluno = ""
maior_nota = 0
for k in notas.keys():
    if notas[k]['programacao'] > maior_nota:
        melhor_aluno = k
print(melhor_aluno)