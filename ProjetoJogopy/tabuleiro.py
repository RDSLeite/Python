LINHAS = 6
COLUNAS = 6

def criar_matriz():
    return [["." for _ in range(COLUNAS)] for _ in range(LINHAS)]

def desenhar_naves(naves):
    mat = criar_matriz()
    for n in naves:
        if n.viva and n.pos:
            r, c = n.pos
            if 0 <= r < LINHAS and 0 <= c < COLUNAS:
                mat[r][c] = f"{n.cor}{n.simbolo}\033[0m"
    return mat

def desenhar_tiros(tiros):
    mat = criar_matriz()
    for r, c in tiros:
        if 0 <= r < LINHAS and 0 <= c < COLUNAS:
            mat[r][c] = "X"
    return mat

def imprimir(mat):
    for linha in mat:
        print(" ".join(linha))
