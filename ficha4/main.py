import sys
sys.dont_write_bytecode = True
from inventario import *

def menu():
    inventario = carregar_inventario()

    while True:
        print("""
========= MENU PRINCIPAL =========
1. Ver inventário
2. Adicionar item
3. Atualizar quantidade
4. Remover item
5. Pesquisa avançada
6. Relatório de stock
7. Guardar e sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_inventario(inventario)
        elif opcao == "2":
            adicionar_item(inventario)
        elif opcao == "3":
            atualizar_quantidade(inventario)
        elif opcao == "4":
            remover_item(inventario)
        elif opcao == "5":
            pesquisa_avancada(inventario)
        elif opcao == "6":
            relatorio_stock(inventario)
        elif opcao == "7":
            guardar_inventario(inventario)
            print("Inventário guardado. A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()