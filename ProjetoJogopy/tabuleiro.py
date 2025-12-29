import random
from nave import *

# Dimensões do tabuleiro
LINHAS = 6
COLUNAS = 6


# Cria uma matriz (lista de listas) preenchida com um símbolo vazio
def criar_matriz(vazia='.'):
    return [[vazia for _ in range(COLUNAS)] for _ in range(LINHAS)]


# Coloca as naves em posições aleatórias do tabuleiro
def colocar_naves_aleatorio(naves):
    # Lista com todas as posições possíveis
    posicoes = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]

    # Baralha as posições
    random.shuffle(posicoes)

    # Atribui uma posição a cada nave
    for i, nav in enumerate(naves):
        nav.pos = posicoes[i]


# Desenha as naves na matriz do tabuleiro
def desenhar_naves(naves):
    mat = criar_matriz()

    for nav in naves:
        # Só desenha naves vivas e com posição definida
        if nav.viva and nav.pos:
            r, c = nav.pos
            cor = CORES.get(nav.cor, "")
            reset = CORES["reset"]
            mat[r][c] = f"{cor}{nav.simbolo}{reset}"

    return mat


# Desenha os tiros efectuados na ronda actual
def desenhar_tiros(lista_tiros):
    mat = criar_matriz()

    for r, c in lista_tiros:
        # Marca o tiro com X
        mat[r][c] = "X"

    return mat


# Imprime o tabuleiro com bordas e coordenadas
def imprimir_com_borda(mat):
    # Cabeçalho das colunas
    print("   " + " ".join(f"{c}" for c in range(COLUNAS)))
    print("  +" + "--"*COLUNAS + "+")

    # Linhas do tabuleiro
    for i, linha in enumerate(mat):
        linha_str = ""
        for c in linha:
            linha_str += f"{c:2}"
        print(f"{i:>2}|{linha_str}|")

    print("  +" + "--"*COLUNAS + "+")


# Gera tiros aleatórios dentro dos limites do tabuleiro
def gerar_tiros_aleatorios(quantidade=3):
    """Gera tiros que podem acertar qualquer posição do tabuleiro"""
    livres = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]

    # Ajusta caso existam menos posições do que tiros pedidos
    if len(livres) < quantidade:
        quantidade = len(livres)

    return random.sample(livres, quantidade)
