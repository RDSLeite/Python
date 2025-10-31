def contar_caracteres(texto):
    d = {}
    for c in texto:
        if c in d.keys():
            d[c] += 1 
        else:
            d[c] = 1
    return d

print(contar_caracteres("Turma de Programacao da oficina"))