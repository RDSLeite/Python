class Cliente:
    totalClientes = 0
    def __init__(self, nome, altura, peso, vip=False):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.vip = vip
        self.pontuacao = 0
        
    def imc(self):
        return self.peso / (self.altura * self.altura)

c1 = Cliente("Marcelo", 1.84,96,True)
Cliente.totalClientes += 1
c2 = Cliente("Ana", 1.65, 64)
Cliente.totalClientes += 1
print(c1.nome)
if c2.vip:
    print("Cliente VIP")
else:
    print("Cliente normal")
print(c1.imc())