# nave.py

CORES = {
    "vermelho": "\033[91m",
    "verde": "\033[92m",
    "amarelo": "\033[93m",
    "azul": "\033[94m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}

class NaveModelo:
    def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str):
        self.nome = nome
        self.cor = cor
        self.energia = 100
        self.perda_energia = perda_energia
        self.simbolo = simbolo
        self.pos = None
        self.viva = True

    def perder_energia(self):
        if not self.viva:
            return self.energia
        self.energia -= self.perda_energia
        if self.energia <= 0:
            self.energia = 0
            self.viva = False
        return self.energia

    def energia_atual(self):
        return self.energia

    def mostrar_dados(self):
        cor = CORES.get(self.cor, "")
        reset = CORES["reset"]
        return f"{cor}{self.nome} {barra_energia(self.energia)} | Energia: {self.energia} | Símbolo: {self.simbolo}{reset}"


class NaveComExtra(NaveModelo):
    def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str, energia_extra: int):
        super().__init__(nome, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def adicionar_energia_extra(self):
        if not self.viva:
            return self.energia
        self.energia += self.energia_extra
        if self.energia > 100:
            self.energia = 100
        return self.energia


# Barra de energia
def barra_energia(energia):
    total = 10
    cheios = int(energia / 10)
    vazios = total - cheios
    return "[" + "█"*cheios + " "*vazios + "]"
