class Pessoa:
    total_pessoas = 0
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoas += 1
        
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"
    
    # Getter para o nome da pessoa
    @property
    def nome(self):
        return self.__nome
    
    # Setter para idade
    @nome.setter
    def nome(self,novo_nome):
        if len(novo_nome) < 2:
            print("Nome inválido")
        else: self.__nome = novo_nome
        
    
    # Getter para a idade da pessoa
    @property
    def idade(self):
        return self.__idade
    
    # Setter para idade
    @idade.setter
    def idade(self,nova_idade):
        if len(nova_idade) < 0:
            print("idade inválida")
        else: self.__nome = nova_idade
    
# AREA DE TESTE
p1 = Pessoa("Marcelo", 52)
p2 = Pessoa("Sergio", 19)
p3 = Pessoa("Tomas", 18)
print(p1.nome)
print(Pessoa.total_pessoas)
print(p2)