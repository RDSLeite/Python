class NaveModelo:
    def __init__(self, denominacao, cor, perda_energia, simbolo):
        self.denominacao = denominacao
        self.cor = cor  # ANSI code da cor
        self.perda_energia = perda_energia
        self.simbolo = simbolo
        self.energia = 100
        self.pos = None
        self.viva = True

    def perder_energia(self):
        if self.viva:
            self.energia -= self.perda_energia
            if self.energia <= 0:
                self.energia = 0
                self.viva = False
        return self.energia

    def energia_atual(self):
        return self.energia

    # ✅ ADICIONADO para evitar AttributeError
    def mostrar_dados(self):
        return f"{self.cor}{self.denominacao} | Energia: {self.energia} | Símbolo: {self.simbolo}\033[0m"


class NaveComExtra(NaveModelo):
    def __init__(self, denominacao, cor, perda_energia, simbolo, energia_extra):
        super().__init__(denominacao, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def adicionar_energia_extra(self):
        if self.viva:
            self.energia += self.energia_extra
            if self.energia > 100:
                self.energia = 100
        return self.energia
