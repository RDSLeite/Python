# x = 5
# print(x)
# print(type(x))
# x = "Rui"
# print(x)
# print(type(x))
# a,b,c = "Rui",8,7
# print(a,b,c)

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
soma = num1 + num2
media = (num1 + num2) / 2
# print ("A soma de ", num1, "com ", num2,"é igual a ",soma)
# print ("A soma de " + str(num1), "com " + str(num2),"é igual a " + str(soma))
#fstring
print(f'A soma de {num1} com {num2} é igual a {soma:.2f}')
print(f'A media de {num1} com {num2} é igual a {media:.2f}')