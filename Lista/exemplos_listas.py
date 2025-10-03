# EXEMPLO 1
#
# Escreva um programa que:
#   1. Crie uma lista vazia
#   2. Preencha a lista com os valores de 1 a 10
#   3. Apresente a soma e a média de todos os valores da lista

lista= []
for i in range(1,11):
    lista.append(i)
soma = sum(lista)# Some os elementos da lista 
print(f"Soma:  {soma}")
total_elem = len(lista) # Devolve o nº de elementos da lista 
media = soma / total_elem
print(f"Media: {media:.2f}")


#################################################################################################################################################################

# EXEMPLO 2
#
# Considere a lista abaixo e escreva um programa que multiplique todos os seus elementos.
lista=[5,4,3,2,1]

m = 1

for i in lista:
    m = m * 1
    
print(f"Resultado:  {m:.2f}")    

#################################################################################################################################################################

# EXEMPLO 3
#
# Considere a lista abaixo e escreva um programa que mostre 
# na tela o seu maior número.

lista=[5,43,3,2,10]
maior = max(lista)
menor = min(lista)

#################################################################################################################################################################

# EXEMPLO 4
#
# Ordene os elementos das listas a seguir: a primeira em ordem crescente e a segunda em ordem decrescente.

nums = [500,123,248,1039,108,311]
letras = ['a','c','b','f','z','x','b']
nums.sort()
print(nums)
letras.sort(reverse=True)
nums.reverse()


#################################################################################################################################################################

# EXEMPLO 5
#
# Considere a lista a seguir e 
# escreva um programa para remover os elementos duplicados.

lista = [1,2,3,1,7,3,2,4,1,3]
lista = list(set(lista))
print(lista)

#################################################################################################################################################################

# EXEMPLO 6
#
# Considere a lista a seguir, que apresenta dados referentes a série temporal de 1900 a 2020. Faça o que se pede:
lista_anos=[1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907,1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915,1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923,1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939,1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,2020]
#   a) Crie uma lista que armazene os 20 primeiros anos da série;
#   b) Crie uma lista que armazene os anos de 1937 a 1969;
#   c) Crie uma lista que armazene o último ano da série;
#   d) Apresente a série temporal de 10 em 10 anos.

#FATIAMENTO
print(lista_anos[:20]) #Alinia a
print(lista_anos[20:])
print(lista_anos.index(1923))
print(lista_anos[lista_anos.index(1937):lista_anos.index(1970)])#Alinia b
print(lista_anos[-1]) # Ultimo elemento da lista 
print(lista_anos[::10])#Alinia d



#################################################################################################################################################################

# EXEMPLO 7
#
# Verifique se uma lista é vazia ou não. Caso a lista seja vazia,
# mostre True na tela, caso contrário False.

lista = []
if len(lista) == 0:
    print(True)
else:
    print(True)
if not lista:
        print(True)
else:
    print(False)
    
nums = [1,2,3]
nums2 = nums.copy()
nums.append(4)
print(nums, nums2)

nums = [1,2,3]
nums2 = nums
nums.append(4)
print(nums, nums2)

#################################################################################################################################################################

# EXEMPLO 8
#
# Imprima apenas os nomes iniciados pela letra A da lista abaixo apresentada.

nomes = ["Ana","Rui","João","Mariana","Alice","Luana"]
#Iniciar pela letra a
for nome in nomes:
    if nome.lower().startswith('a'):
        print(nome)
#Termine com a letra o
for nome in nomes:
    if nome.lower().endswith('o'):
        print(nome)
#################################################################################################################################################################

# EXEMPLO 9
#
# Utilizando a lista criada anteriormente, liste os nomes terminados com a letra o.
# Utilizando a mesma lista, liste os nomes que contenham 'ana' no nome.

for nome in nomes:
    if 'ana' in nome.lower():
        print(nome)
        
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1.extend(lista2)
lista1.remove(2)
lista1.clear()
nomes.remove("Ana")