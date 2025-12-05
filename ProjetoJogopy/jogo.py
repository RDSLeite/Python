# main.py

from nave import *
from tabuleiro import *
from funcao import *
import os

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

def iniciar_jogo():
    naves = criar_naves()
    loop_jogo(naves)

def loop_jogo(naves, total_tiros=0, total_certos=0):
    energia_extra_usada = False

    while True:
        limpar_ecra()

        # Mover naves para novas posições
        colocar_naves_aleatorio(naves)

        # Gerar tiros automáticos (podem acertar qualquer posição)
        tiros = gerar_tiros_aleatorios(3)
        total_tiros += len(tiros)

        # Verificar acertos e aplicar dano
        for tiro in tiros:
            for nav in naves:
                if nav.viva and nav.pos == tiro:
                    nav.perder_energia()
                    total_certos += 1
                    print(f"Acertou a nave {nav.nome}! -{nav.perda_energia} energia")

        # Energia extra ao atingir 45 tiros
        if total_tiros >= 45 and not energia_extra_usada:
            for nav in naves:
                if hasattr(nav, "adicionar_energia_extra"):
                    nav.adicionar_energia_extra()
            energia_extra_usada = True

        # Exibir tabuleiros
        print("\nTABULEIRO - NAVES")
        imprimir_com_borda(desenhar_naves(naves))

        print("\nTABULEIRO - TIROS (rodada atual)")
        imprimir_com_borda(desenhar_tiros(tiros))

        # Dados das naves
        print("\nDADOS DAS NAVES:")
        for nav in naves:
            print(nav.mostrar_dados())

        # Estatísticas
        print(f"\nTiros totais: {total_tiros}")
        print(f"Certeiros: {total_certos}")
        print(f"Eficácia: {eficacia(total_tiros, total_certos):.2f}%")

        input("\nENTER para continuar...")

        # Fim do jogo
        if all(not n.viva for n in naves) or total_tiros >= 105:
            print("Jogo terminado.")
            input()
            return

def menu():
    capa()
    naves = criar_naves()
    total_tiros = 0
    total_certos = 0

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
            if os.path.exists(SAVE):
                naves, total_tiros, total_certos = carregar_jogo(SAVE, NaveModelo, NaveComExtra)
                loop_jogo(naves, total_tiros, total_certos)
            else:
                print("Nenhum jogo guardado.")
                input()
        elif op == "3":
            guardar_jogo(SAVE, naves, total_tiros, total_certos)
            print("Jogo guardado.")
            input()
        elif op == "4":
            break

if __name__ == "__main__":
    menu()
