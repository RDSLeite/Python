# tabuleiro.py

import random
from nave import *

LINHAS = 6
COLUNAS = 6

def criar_matriz(vazia='.'):
    return [[vazia for _ in range(COLUNAS)] for _ in range(LINHAS)]

def colocar_naves_aleatorio(naves):
    posicoes = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]
    random.shuffle(posicoes)

    for i, nav in enumerate(naves):
        nav.pos = posicoes[i]

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
        mat[r][c] = "X"  # símbolo simples para manter alinhamento
    return mat

def imprimir_com_borda(mat):
    print("   " + " ".join(f"{c}" for c in range(COLUNAS)))
    print("  +" + "--"*COLUNAS + "+")
    for i, linha in enumerate(mat):
        linha_str = ""
        for c in linha:
            linha_str += f"{c:2}"
        print(f"{i:>2}|{linha_str}|")
    print("  +" + "--"*COLUNAS + "+")

def gerar_tiros_aleatorios(quantidade=3):
    """Gera tiros que podem acertar qualquer posição do tabuleiro"""
    livres = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)]
    if len(livres) < quantidade:
        quantidade = len(livres)
    return random.sample(livres, quantidade)
