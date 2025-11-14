# main.py

# Importa o módulo sys para alterar configurações internas do Python
import sys

# Impede o Python de criar ficheiros .pyc e a pasta __pycache__
sys.dont_write_bytecode = True

# Importa todas as funções do ficheiro inventario.py
# (carregar, guardar, adicionar, remover, etc.)
from inventario import *


def menu():
    """Função principal que mostra o menu e executa as opções."""

    # Carrega o inventário do ficheiro JSON
    inventario = carregar_inventario()

    # Loop infinito do menu, só termina quando o utilizador escolher "7"
    while True:
        # Mostra as opções disponíveis ao utilizador
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

        # Recolhe a escolha do utilizador
        opcao = input("Escolha uma opção: ")

        # Ver inventário
        if opcao == "1":
            ver_inventario(inventario)

        # Adicionar novo item
        elif opcao == "2":
            adicionar_item(inventario)

        # Atualizar quantidade de um item existente
        elif opcao == "3":
            atualizar_quantidade(inventario)

        # Remover item do inventário
        elif opcao == "4":
            remover_item(inventario)

        # Pesquisa avançada por título ou autor
        elif opcao == "5":
            pesquisa_avancada(inventario)

        # Relatório com o valor total do stock
        elif opcao == "6":
            relatorio_stock(inventario)

        # Guardar inventário e sair do programa
        elif opcao == "7":
            guardar_inventario(inventario)
            print("Inventário guardado. A sair...")
            break  # Sai do loop e termina o programa

        # Caso o utilizador escreva algo inválido
        else:
            print("Opção inválida. Tente novamente.\n")


# Esta condição garante que o menu só executa se o ficheiro for iniciado diretamente,
# e não quando for importado como módulo noutro ficheiro.
if __name__ == "__main__":
    menu()
