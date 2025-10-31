# Dicionario em que as chaves vão de 1 a 20 e o valor é a chave mais 10 :
d = {n: n+10 for n in range(1,21)}
print(d)
aluno = {'matematica' : 12, 'informática': 15, 'portugues':  17}
notas_maiores_ou_igual_a_15 ={c: v for c,v in aluno.items() if v >= 15}
print(notas_maiores_ou_igual_a_15) 

nomes = ["Alicate","Chave de fendas","Martelo","Furadeira"]
dict_nomes = {f: len(f) for f in nomes}
print(dict_nomes)