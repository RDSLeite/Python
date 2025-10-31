# aluno = {
#     'nome':'João Paulo',
#     'naturalidade':'Portugagl',
#     'peso':84,
#     'aprovado': True
# }

# #imprimir uma chave do dicionario
# print(aluno['naturalidade']) # Portugal
# print(f'O aluno  {aluno['nome']} tem peso {aluno['peso']}kg.') # Portugal

# # Caracteristicas do aluno 
# for chave in aluno.keys():
#     print(chave)

# #Valores das chaves
# for v in aluno.values():
#     print(v)

# # Par chave /valor
# for k,v in aluno.items():
#     print(f"{k}: {v}")
    
# aluno['imc'] = round (aluno['peso'] / (aluno['altura'] * aluno['altura']),2)
# aluno['naturalidade']= 'Itália'
# print(aluno)

d = {}
d = dict() # Dicionario vazio
d1 = dict(nome="Rui",idade = 50)
d2 = {'nome':'Rui','idade': 50}
#d = dict([('nome','rui'),('idade',50)])

d1['idade'] = 51
idade = d1.get('idade2','idade desconhecida')
print(idade)

for chave in d2.keys():
    print(chave)# nome, idade
for v in d2.values():
    print(v)
for c,v in d2.items():
    print(f"{c} com valor {v}")
    
produtos = {
    'casaco': {'preco': 23.99, 'iva': 0.23},
    'camisa': {'preco': 71.99, 'iva': 0.13},
    'sapato': {'preco': 55.99, 'iva': 0.23},
}

print(sorted(produtos))