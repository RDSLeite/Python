aluno = {
    'nome':'Ana Silva',
    'Idade': 17,
    'Disciplinas':['Matemática','Física','Informática'],
    'notas': {"Matemática": 18, "Física": 17, "Informática": 19},
}

aluno['Disciplinas'].append('Portugues')
aluno['notas']['Portugues'] = 16
aluno['Idade'] = 18

notas_aluno = aluno['notas']
notas = [nota for nota in notas_aluno.values()]
media = sum(notas)/len(notas)
print(aluno)
print(f"Media final = {media:.2f} valores")