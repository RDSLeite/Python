# funcao.py

import json
import os
from nave import *

SAVE = "save.json"

def limpar_ecra():
    os.system("cls" if os.name == "nt" else "clear")

def guardar_jogo(caminho, naves, total_tiros, total_certos):
    dados = {
        "naves": [],
        "total_tiros": total_tiros,
        "total_certos": total_certos
    }

    for n in naves:
        dados["naves"].append({
            "nome": n.nome,
            "cor": n.cor,
            "energia": n.energia,
            "perda_energia": n.perda_energia,
            "simbolo": n.simbolo,
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
            nav = NaveComExtra(
                info["nome"], info["cor"], info["perda_energia"],
                info["simbolo"], info["energia_extra"]
            )
        else:
            nav = NaveModelo(
                info["nome"], info["cor"], info["perda_energia"],
                info["simbolo"]
            )
        nav.energia = info["energia"]
        nav.viva = info["viva"]
        nav.pos = tuple(info["pos"]) if info["pos"] else None
        naves.append(nav)

    return naves, dados["total_tiros"], dados["total_certos"]

def eficacia(total, certos):
    return (certos * 100 / total) if total > 0 else 0
