from nave import NaveModelo, NaveComExtra
from funcao import gerar_tiros_aleatorios, eficacia, limpar_ecra, guardar_jogo, carregar_jogo
from tabuleiro import desenhar_naves, desenhar_tiros, imprimir, LINHAS, COLUNAS
import random
import os

SAVE_FILE = "save_jogo.json"

def capa():
    limpar_ecra()
    print("="*50)
    print("       JOGO DAS NAVES".center(50))
    print("       2P-TrabAv01-NomeFormando".center(50))
    print("="*50)
    input("Prima Enter para continuar...")

def menu():
    while True:
        limpar_ecra()
        print("MENU PRINCIPAL")
        print("1) Iniciar Jogo")
        print("2) Carregar Jogo")
        print("3) Guardar Jogo")
        print("4) Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            iniciar_jogo()
        elif op == "2":
            if os.path.exists(SAVE_FILE):
                naves, tiros, total_tiros, total_certos = carregar_jogo(SAVE_FILE, NaveModelo, NaveComExtra)
                loop_jogo(naves, tiros, total_tiros, total_certos)
            else:
                print("Ficheiro de save não encontrado.")
                input("Enter para continuar...")
        elif op == "3":
            try:
                guardar_jogo(SAVE_FILE, naves, tiros, total_tiros, total_certos)
                print("Jogo guardado.")
            except:
                print("Nenhum jogo em memória para guardar.")
            input("Enter para continuar...")
        elif op == "4":
            break

def criar_naves_iniciais():
    n1 = NaveModelo("Falcon", "\033[91m", 20, "F")  # vermelho
    n2 = NaveComExtra("Guardian", "\033[92m", 15, "G", 20)  # verde
    n3 = NaveComExtra("Viper", "\033[93m", 10, "V", 25)  # amarelo
    return [n1, n2, n3]

def posicionar_naves_aleatorio(naves):
    poss = [(r,c) for r in range(LINHAS) for c in range(COLUNAS)]
    random.shuffle(poss)
    for n, p in zip(naves, poss):
        n.pos = p

def loop_jogo(naves, tiros, total_tiros, total_certos):
    while True:
        limpar_ecra()
        print("Inserindo 3 tiros aleatórios...")
        novos_tiros = gerar_tiros_aleatorios(tiros, 3)
        if len(novos_tiros) == 0:
            print("Não há mais casas livres para tiros. Fim de jogo.")
            input("Enter para voltar ao menu...")
            return
        tiros.extend(novos_tiros)
        total_tiros += len(novos_tiros)

        # Acertos
        for tiro in novos_tiros:
            for n in naves:
                if n.viva and n.pos == tiro:
                    n.perder_energia()

        total_certos = sum(1 for tiro in tiros for n in naves if n.pos == tiro and n.viva)

        # Energia extra após 45 tiros
        if total_tiros >= 45 and total_tiros - len(novos_tiros) < 45:
            for n in naves:
                if hasattr(n, "adicionar_energia_extra"):
                    n.adicionar_energia_extra()

        # Mostrar tabuleiros
        print("\nTABULEIRO - NAVES")
        imprimir(desenhar_naves(naves))
        print("\nTABULEIRO - TIROS")
        imprimir(desenhar_tiros(tiros))
        print("\nDADOS DAS NAVES:")
        for n in naves:
            print(n.mostrar_dados())

        print(f"\nTotal tiros: {total_tiros}")
        print(f"Tiros certeiros: {total_certos}")
        print(f"Eficácia: {eficacia(total_tiros, total_certos):.2f}%")
        input("Prima Enter para continuar...")

        if all(not n.viva for n in naves):
            print("Todas as naves foram aniquiladas. Fim de jogo.")
            input("Enter para voltar ao menu...")
            return
        if total_tiros >= 105:
            print("Limite de 105 tiros atingido. Fim de jogo.")
            input("Enter para voltar ao menu...")
            return

def iniciar_jogo():
    global naves, tiros, total_tiros, total_certos
    naves = criar_naves_iniciais()
    posicionar_naves_aleatorio(naves)
    tiros = []
    total_tiros = 0
    total_certos = 0
    loop_jogo(naves, tiros, total_tiros, total_certos)

if __name__ == "__main__":
    capa()
    menu()
