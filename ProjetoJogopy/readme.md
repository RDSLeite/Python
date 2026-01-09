🚀 Projeto: Jogo das Naves – Relatório Técnico
📌 1. Introdução

O projeto Jogo das Naves foi desenvolvido em Python 3 e tem como objetivo criar um jogo de estratégia em modo consola onde o jogador interage com naves espaciais em um tabuleiro, realizando tiros automáticos ou manuais para destruir as naves adversárias.

O projeto foi construído com base em:

Programação Orientada a Objetos (POO)

Gestão de estados com ficheiros JSON

Experiência de utilizador com cores ANSI e mensagens visuais

Estrutura modular, com múltiplos ficheiros (jogo.py, nave.py, tabuleiro.py, funcao.py)

📂 2. Estrutura de Ficheiros
projeto/
│
├── jogo.py        # Ficheiro principal (menu e loop do jogo)
├── nave.py        # Classes das naves
├── tabuleiro.py   # Lógica e desenho do tabuleiro
├── funcao.py      # Funções auxiliares (guardar, carregar, etc.)
├── saves/         # Pasta de jogos guardados
└── README.md      # Relatório e documentação


Explicação:

jogo.py → Contém o loop do jogo, opções de tiro, menu e interações

nave.py → Define as classes das naves (base e com energia extra)

tabuleiro.py → Desenha tabuleiros e trata posições e tiros

funcao.py → Guarda e carrega o estado do jogo

saves/ → Armazena os ficheiros JSON com saves automáticos ou manuais

🛸 3. Classes das Naves (nave.py)
🔹 3.1 Classe Base NaveModelo
class NaveModelo:
    def __init__(self, nome, cor, perda_energia, simbolo):
        self.nome = nome
        self.cor = cor
        self.energia = 100
        self.perda_energia = perda_energia
        self.simbolo = simbolo
        self.pos = None
        self.viva = True

    def perder_energia(self):
        if not self.viva:
            return
        self.energia -= self.perda_energia
        if self.energia <= 0:
            self.energia = 0
            self.viva = False

    def mostrar_dados(self):
        cor = CORES.get(self.cor, "")
        reset = CORES["reset"]
        return f"{cor}{self.nome} {barra_energia(self.energia)} | Energia: {self.energia} | Símbolo: {self.simbolo}{reset}"


Descrição:

perder_energia() → Reduz a energia da nave e atualiza estado

mostrar_dados() → Retorna uma string formatada com barra de energia e cor

🔹 3.2 Classe NaveComExtra (herança)
class NaveComExtra(NaveModelo):
    def __init__(self, nome, cor, perda_energia, simbolo, energia_extra):
        super().__init__(nome, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def adicionar_energia_extra(self):
        if not self.viva:
            return
        self.energia += self.energia_extra
        if self.energia > 100:
            self.energia = 100


Permite adicionar energia extra após um certo número de tiros

Mantém compatibilidade com a barra de energia visual

🗺️ 4. Tabuleiro e Tiros (tabuleiro.py)
🔹 4.1 Dimensões
LINHAS = 6
COLUNAS = 6


O tabuleiro é 6x6, mas pode ser facilmente alterado

🔹 4.2 Criação de Matriz
def criar_matriz(vazia='.'):
    return [[vazia for _ in range(COLUNAS)] for _ in range(LINHAS)]


Matriz inicializada com .

Usada tanto para naves como para tiros

🔹 4.3 Colocação Aleatória de Naves
def colocar_naves_aleatorio(naves):
    posicoes = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]
    random.shuffle(posicoes)
    for i, nav in enumerate(naves):
        nav.pos = posicoes[i]


Evita sobreposição de posições

Cada ronda reposiciona todas as naves

🔹 4.4 Desenho de Naves e Tiros
def desenhar_naves(naves):
    mat = criar_matriz()
    for nav in naves:
        if nav.viva and nav.pos:
            r, c = nav.pos
            cor = CORES.get(nav.cor, "")
            reset = CORES["reset"]
            mat[r][c] = f"{cor}{nav.simbolo}{reset}"
    return mat

def desenhar_tiros(lista_tiros):
    mat = criar_matriz()
    for r, c in lista_tiros:
        mat[r][c] = "X"
    return mat

🔹 4.5 Impressão com Bordas
def imprimir_com_borda(mat):
    print("   " + " ".join(f"{c}" for c in range(COLUNAS)))
    print("  +" + "--"*COLUNAS + "+")
    for i, linha in enumerate(mat):
        linha_str = ""
        for c in linha:
            linha_str += f"{c:2}"
        print(f"{i:>2}|{linha_str}|")
    print("  +" + "--"*COLUNAS + "+")


Adiciona coordenadas visuais para fácil referência

Melhora UX no terminal

🔹 4.6 Geração de Tiros Aleatórios
def gerar_tiros_aleatorios(quantidade=3):
    livres = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]
    return random.sample(livres, quantidade)


Permite até 3 tiros por ronda

Garante que não haja repetição

🎮 5. Loop Principal (loop_jogo)
while True:
    colocar_naves_aleatorio(naves)
    if modo_tiros == "1":
        tiros = gerar_tiros_aleatorios(3)
    elif modo_tiros == "2":
        # input manual do jogador
        ...

🔹 Funcionalidades do Loop:

Reposicionamento de naves

Escolha do modo de tiro (automático/manual)

Verificação de acertos com mensagens 💥

Atualização da barra de energia e dados da nave

Exibição do tabuleiro e estatísticas

Opções do jogador: Continuar, Guardar, Sair

Fim de jogo:

Todas as naves destruídas

Limite de 105 tiros atingido

🔹 Mensagens de Acerto
mensagens_acerto[nav.nome] = f"💥 Acertou {nav.nome}! Energia -{nav.perda_energia}"


Mostram-se ao lado dos dados da nave

Pequeno efeito visual com sleep(0.2) entre tiros

Exemplo no terminal:

Falcon   [██████    ] | Energia: 60 | Símbolo: F   💥 Acertou Falcon! Energia -20
Guardian [████████  ] | Energia: 85 | Símbolo: G
Viper    [███████   ] | Energia: 70 | Símbolo: V

💾 6. Guardar e Carregar Jogo (funcao.py)
🔹 Guardar Jogo Manual
guardar_jogo("saves/save_1.json", naves, total_tiros, total_certos)


Guarda estado atual do jogo

Pode guardar no mesmo ficheiro se estiver a continuar o mesmo jogo

Permite criar novo ficheiro se iniciar um novo jogo

🔹 Carregar Jogo
naves, total_tiros, total_certos = carregar_jogo(
    ficheiro, NaveModelo, NaveComExtra
)


Restaura posição, energia e estado de cada nave

Mantém estatísticas do jogo e o modo de tiro escolhido

📊 7. Estatísticas do Jogo

Tiros totais

Certeiros

Eficácia (%)

def eficacia(total, certos):
    return (certos * 100 / total) if total > 0 else 0


Exemplo de apresentação:

Tiros totais: 18
Certeiros: 9
Eficácia: 50.00%

✅ 8. Funcionalidades Extras

Escolha do modo de tiro: manual ou automático

Mensagens de acerto animadas

Barras de energia coloridas

Histórico de saves com data e hora

Limite máximo de tiros

Energia extra para naves especiais após 45 tiros

🎨 9. Melhorias Visuais

Uso de cores ANSI para diferenciar naves

Barra de energia [█████ ]

Mensagens 💥 visíveis ao lado das naves

📌 10. Conclusão

O projeto demonstra:

Organização modular do código

Aplicação de POO e herança

Persistência de estado em ficheiros JSON

Interatividade e UX em terminal

Gestão de eventos como tiros, destruição de naves, energia extra e salvamentos

Este relatório detalhado serve como documentação técnica e explicativa para o projeto Jogo das Naves.
