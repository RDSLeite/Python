import random
import os
import json
from tabuleiro import LINHAS, COLUNAS

def limpar_ecra():
    os.system("cls" if os.name == "nt" else "clear")

def gerar_tiros_aleatorios(existentes, quantidade=3):
    proibidas = set(existentes)
    possiveis = [(r, c) for r in range(LINHAS) for c in range(COLUNAS)
                 if (r, c) not in proibidas]
    if len(possiveis) == 0:
        return []
    if len(possiveis) < quantidade:
        quantidade = len(possiveis)
    return random.sample(possiveis, quantidade)

def guardar_jogo(caminho, naves, tiros, total_tiros, total_certos):
    dados = {"naves": [], "tiros": tiros, "total_tiros": total_tiros, "total_certos": total_certos}
    for n in naves:
        dados["naves"].append({
            "denominacao": n.denominacao,
            "cor": n.cor,
            "perda_energia": n.perda_energia,
            "simbolo": n.simbolo,
            "energia": n.energia,
            "pos": n.pos,
            "viva": n.viva,
            **({"energia_extra": n.energia_extra} if hasattr(n, "energia_extra") else {})
        })
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def carregar_jogo(caminho, NaveModelo, NaveComExtra):
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    naves = []
    for info in dados["naves"]:
        if "energia_extra" in info:
            nav = NaveComExtra(info["denominacao"], info["cor"], info["perda_energia"],
                               info["simbolo"], info["energia_extra"])
        else:
            nav = NaveModelo(info["denominacao"], info["cor"], info["perda_energia"], info["simbolo"])
        nav.energia = info["energia"]
        nav.viva = info["viva"]
        nav.pos = tuple(info["pos"]) if info["pos"] else None
        naves.append(nav)
    tiros = [tuple(t) for t in dados["tiros"]]
    return naves, tiros, dados["total_tiros"], dados["total_certos"]

def eficacia(total_tiros, total_certos):
    if total_tiros == 0:
        return 0.0
    return (total_certos * 100) / total_tiros
