# Códigos de cores ANSI para o terminal
CORES = {
    "vermelho": "\033[91m",
    "verde": "\033[92m",
    "amarelo": "\033[93m",
    "azul": "\033[94m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}


# ----------------- CLASSE BASE DAS NAVES -----------------
class NaveModelo:
    def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str):
        # Nome da nave
        self.nome = nome

        # Cor da nave (usada para visual)
        self.cor = cor

        # Energia inicial
        self.energia = 100

        # Energia perdida por cada acerto
        self.perda_energia = perda_energia

        # Símbolo no tabuleiro
        self.simbolo = simbolo

        # Posição actual no tabuleiro
        self.pos = None

        # Estado da nave
        self.viva = True


    # Reduz a energia da nave quando é atingida
    def perder_energia(self):
        if not self.viva:
            return self.energia

        self.energia -= self.perda_energia

        # Se a energia chegar a zero, a nave morre
        if self.energia <= 0:
            self.energia = 0
            self.viva = False

        return self.energia


    # Devolve a energia actual da nave
    def energia_atual(self):
        return self.energia


    # Devolve uma string com os dados da nave formatados
    def mostrar_dados(self):
        cor = CORES.get(self.cor, "")
        reset = CORES["reset"]
        return f"{cor}{self.nome} {barra_energia(self.energia)} | Energia: {self.energia} | Símbolo: {self.simbolo}{reset}"


# ----------------- NAVE COM ENERGIA EXTRA -----------------
class NaveComExtra(NaveModelo):
    def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str, energia_extra: int):
        # Inicializa a nave base
        super().__init__(nome, cor, perda_energia, simbolo)

        # Quantidade de energia extra
        self.energia_extra = energia_extra


    # Adiciona energia extra à nave
    def adicionar_energia_extra(self):
        if not self.viva:
            return self.energia

        self.energia += self.energia_extra

        # Limita a energia máxima a 100
        if self.energia > 100:
            self.energia = 100

        return self.energia


# ----------------- BARRA DE ENERGIA -----------------
def barra_energia(energia):
    total = 10
    cheios = int(energia / 10)
    vazios = total - cheios

    # Representação gráfica da energia
    return "[" + "█"*cheios + " "*vazios + "]"
