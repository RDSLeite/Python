import json
import os
from nave import *

SAVE_FOLDER = "saves"

# Cria a pasta de saves se não existir
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# ----------------- LIMPAR TELA -----------------
def limpar_ecra():
    os.system("cls" if os.name == "nt" else "clear")

# ----------------- GUARDAR JOGO -----------------
def guardar_jogo(caminho, naves, total_tiros, total_certos):
    dados = {
        "naves": [],
        "total_tiros": total_tiros,
        "total_certos": total_certos
    }

    for nav in naves:
        dados["naves"].append({
            "classe": type(nav).__name__,
            "nome": nav.nome,
            "cor": nav.cor,
            "energia": nav.energia,
            "perda_energia": nav.perda_energia,
            "simbolo": nav.simbolo,
            "energia_extra": getattr(nav, "energia_extra", 0),
            "viva": nav.viva,
            "pos": nav.pos
        })

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
    print(f"Jogo guardado em: {caminho}")

# ----------------- GUARDAR JOGO AUTOMÁTICO -----------------
def guardar_jogo_auto(naves, total_tiros, total_certos):
    # descobrir número do próximo save
    existentes = [
        f for f in os.listdir(SAVE_FOLDER)
        if f.startswith("save_") and f.endswith(".json")
    ]
    numero = len(existentes) + 1
    ficheiro = os.path.join(SAVE_FOLDER, f"save_{numero}.json")
    guardar_jogo(ficheiro, naves, total_tiros, total_certos)
    return ficheiro  # retorna o nome do ficheiro criado

# ----------------- CARREGAR JOGO -----------------
def carregar_jogo(ficheiro, NaveModelo, NaveComExtra):
    with open(ficheiro, "r", encoding="utf-8") as f:
        dados = json.load(f)

    naves = []

    for d in dados["naves"]:
        # compatível com saves antigos
        classe = d.get("classe", "NaveModelo")
        if classe == "NaveModelo":
            nav = NaveModelo(d["nome"], d["cor"], d["perda_energia"], d["simbolo"])
        else:
            nav = NaveComExtra(d["nome"], d["cor"], d["perda_energia"], d["simbolo"], d.get("energia_extra", 0))

        nav.energia = d["energia"]
        nav.viva = d["viva"]
        nav.pos = tuple(d["pos"]) if d.get("pos") else None
        naves.append(nav)

    return naves, dados["total_tiros"], dados["total_certos"]

# ----------------- ESCOLHER SAVE -----------------
def escolher_save():
    saves = [
        f for f in os.listdir(SAVE_FOLDER)
        if f.startswith("save_") and f.endswith(".json")
    ]

    if not saves:
        return None

    print("SAVES DISPONÍVEIS:\n")
    for i, s in enumerate(saves, 1):
        print(f"{i} - {s}")

    escolha = input("\nEscolhe o save: ")

    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(saves):
        print("Opção inválida.")
        return None

    return os.path.join(SAVE_FOLDER, saves[int(escolha) - 1])

# ----------------- EFICÁCIA -----------------
def eficacia(total, certos):
    return (certos * 100 / total) if total > 0 else 0
