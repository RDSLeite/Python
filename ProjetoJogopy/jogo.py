from nave import *
from tabuleiro import *
from funcao import *
import os
import time
from datetime import datetime

def criar_naves():
    n1 = NaveModelo("Falcon", "vermelho", 20, "F")
    n2 = NaveComExtra("Guardian", "azul", 15, "G", 20)
    n3 = NaveComExtra("Viper", "magenta", 10, "V", 25)
    return [n1, n2, n3]

def capa():
    limpar_ecra()
    print("=" * 40)
    print("    JOGO DAS NAVES".center(40))
    print("=" * 40)
    input("ENTER para continuar...")

# ----------------- LOOP DE JOGO -----------------
def loop_jogo(naves, total_tiros=0, total_certos=0, ficheiro_atual=None):
    import time

    energia_extra_usada = False

    CORES = {
        "Falcon": "\033[90m",   # cinzento
        "Guardian": "\033[94m", # azul
        "Viper": "\033[95m",    # magenta
        "reset": "\033[0m"
    }

    # Escolha do modo de tiro apenas no início
    print("\nEscolha o modo de tiros:")
    print("1 - Tiros automáticos (3 tiros aleatórios)")
    print("2 - Tiros manuais (digite as coordenadas)")
    modo_tiros = input("Escolha: ")
    if modo_tiros not in ["1","2"]:
        modo_tiros = "1"  # padrão automático

    while True:
        limpar_ecra()

        # Mover naves aleatoriamente
        colocar_naves_aleatorio(naves)

        # Determinar tiros da rodada
        tiros = []

        if modo_tiros == "1":  # automático
            tiros = gerar_tiros_aleatorios(3)

        elif modo_tiros == "2":  # manual
            for i in range(3):
                while True:
                    try:
                        coord = input(f"Digite coordenada do tiro {i+1} (linha,coluna): ")
                        r, c = map(int, coord.strip().split(","))
                        if 0 <= r < 10 and 0 <= c < 10:
                            tiros.append((r, c))
                            break
                        else:
                            print("Coordenadas inválidas. Linha e coluna de 0 a 9.")
                    except:
                        print("Formato inválido. Use linha,coluna (ex: 3,4).")

        total_tiros += len(tiros)

        # Mensagens de acerto
        mensagens_acerto = {}

        for tiro in tiros:
            for nav in naves:
                if nav.viva and nav.pos == tiro:
                    nav.perder_energia()
                    total_certos += 1
                    mensagens_acerto[nav.nome] = f"💥 Acertou {nav.nome}! Energia -{nav.perda_energia}"
                    time.sleep(0.2)

        # Energia extra automática aos 45 tiros
        if total_tiros >= 45 and not energia_extra_usada:
            for nav in naves:
                if hasattr(nav, "adicionar_energia_extra"):
                    nav.adicionar_energia_extra()
            energia_extra_usada = True

        # Exibir tabuleiros
        print("\nTABULEIRO - NAVES")
        imprimir_com_borda(desenhar_naves(naves))

        print("\nTABULEIRO - TIROS (rodada atual)")
        imprimir_com_borda(desenhar_tiros(tiros))  # limpa a cada rodada

        # Mostrar dados das naves com barra de energia e mensagens de acerto
        print("\nDADOS DAS NAVES:")
        for nav in naves:
            cor = CORES.get(nav.nome, "")
            reset = CORES["reset"]
            barra = barra_energia(nav.energia)
            msg = mensagens_acerto.get(nav.nome, "")
            print(f"{cor}{nav.nome:<8} {barra} | Energia: {nav.energia} | Símbolo: {nav.simbolo}   {msg}{reset}")

        # Estatísticas
        print(f"\nTiros totais: {total_tiros}")
        print(f"Certeiros: {total_certos}")
        print(f"Eficácia: {eficacia(total_tiros, total_certos):.2f}%")

        # Instruções visíveis
        print("\nOpções:")
        print("ENTER = Continuar rodada")
        print("1 = Continuar")
        print("2 = Guardar jogo")
        print("3 = Sair do jogo")

        escolha = input("Escolha: ")

        if escolha == "" or escolha == "1":
            pass  # continua para a próxima rodada

        elif escolha == "2":
            if ficheiro_atual:
                guardar_jogo(ficheiro_atual, naves, total_tiros, total_certos)
            else:
                ficheiro_atual = guardar_jogo_auto(naves, total_tiros, total_certos)
            sair = input("Quer sair do jogo? (s/n): ").lower()
            if sair == "s":
                print("Saindo do jogo...")
                input()
                return
            continue

        elif escolha == "3":
            print("Saindo do jogo...")
            input()
            return

        # Fim do jogo
        if all(not n.viva for n in naves):
            print("Todas as naves destruídas.")
            input()
            return

        # Limite de tiros
        if total_tiros >= 105:
            print("Limite de tiros atingido (105).")
            input()
            return
# ----------------- HISTÓRICO DE SAVES -----------------
def escolher_save_com_horario():
    saves = [
        f for f in os.listdir("saves")
        if f.startswith("save_") and f.endswith(".json")
    ]

    if not saves:
        return None

    print("SAVES DISPONÍVEIS:\n")
    for i, s in enumerate(saves, 1):
        caminho = os.path.join("saves", s)
        hora = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%d/%m/%Y %H:%M")
        print(f"{i} - {s} ({hora})")

    escolha = input("\nEscolhe o save: ")

    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(saves):
        print("Opção inválida.")
        return None

    return os.path.join("saves", saves[int(escolha) - 1])

# ----------------- INICIAR NOVO JOGO -----------------
def iniciar_jogo():
    naves = criar_naves()
    loop_jogo(naves)

# ----------------- MENU PRINCIPAL -----------------
def menu():
    capa()
    while True:
        limpar_ecra()
        print("MENU")
        print("1 - Iniciar jogo")
        print("2 - Carregar jogo")
        print("3 - Guardar jogo")
        print("4 - Sair")
        op = input("Opção: ")

        if op == "1":
            iniciar_jogo()

        elif op == "2":
            ficheiro = escolher_save_com_horario()
            if ficheiro:
                naves, total_tiros, total_certos = carregar_jogo(ficheiro, NaveModelo, NaveComExtra)
                loop_jogo(naves, total_tiros, total_certos, ficheiro_atual=ficheiro)
            else:
                print("Nenhum save encontrado.")
                input()

        elif op == "3":
            print("Para guardar, entre no jogo primeiro.")
            input()

        elif op == "4":
            break

if __name__ == "__main__":
    menu()
