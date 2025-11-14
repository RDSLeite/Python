# inventario.py
import json
import os


FICHEIRO = "ficha4/inventario.json"


# ============================
# 1. CARREGAR E GUARDAR DADOS
# ============================

def carregar_inventario():
    if not os.path.exists(FICHEIRO):
        return []

    try:
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_inventario(inventario):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)


# ============================
# 2. FUNÇÕES AUXILIARES
# ============================

def gerar_novo_id(inventario):
    if not inventario:
        return 1
    return max(item["id"] for item in inventario) + 1


def input_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("O valor deve ser positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida.")


def input_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("O valor deve ser positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida.")


def encontrar_item_por_id(inventario, id_item):
    for item in inventario:
        if item["id"] == id_item:
            return item
    return None


# ============================
# 3. OPERAÇÕES CRUD
# ============================

def ver_inventario(inventario):
    if not inventario:
        print("\nInventário vazio.\n")
        return

    print("\n======= INVENTÁRIO =======")
    print(f"{'ID':<5}{'Título':<30}{'Autor':<25}{'Qtd':<5}{'Preço (€)':<10}")
    print("-" * 75)

    for item in inventario:
        print(f"{item['id']:<5}{item['titulo']:<30}{item['autor']:<25}{item['quantidade']:<5}{item['preco']:<10.2f}")

    print()


def adicionar_item(inventario):
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Título: ")
    autor = input("Autor: ")
    quantidade = input_inteiro_positivo("Quantidade: ")
    preco = input_float_positivo("Preço (€): ")

    novo_item = {
        "id": gerar_novo_id(inventario),
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        "preco": preco
    }

    inventario.append(novo_item)
    print("Livro adicionado com sucesso!\n")


def atualizar_quantidade(inventario):
    print("\n--- Atualizar Quantidade ---")
    id_item = input_inteiro_positivo("ID do livro: ")

    item = encontrar_item_por_id(inventario, id_item)
    if not item:
        print("Item não encontrado.\n")
        return

    nova_quantidade = input_inteiro_positivo("Nova quantidade: ")
    item["quantidade"] = nova_quantidade

    print("Quantidade atualizada com sucesso!\n")


def remover_item(inventario):
    print("\n--- Remover Item ---")
    id_item = input_inteiro_positivo("ID do livro: ")

    item = encontrar_item_por_id(inventario, id_item)
    if not item:
        print("Item não encontrado.\n")
        return

    inventario.remove(item)
    print("Item removido com sucesso!\n")


def pesquisa_avancada(inventario):
    termo = input("Pesquisar por título ou autor: ").lower()

    resultados = [
        item for item in inventario
        if termo in item["titulo"].lower() or termo in item["autor"].lower()
    ]

    if not resultados:
        print("Nenhum resultado encontrado.\n")
        return

    print("\nResultados da pesquisa:")
    ver_inventario(resultados)


def relatorio_stock(inventario):
    total = sum(item["quantidade"] * item["preco"] for item in inventario)
    print(f"\nValor total do inventário: {total:.2f} €\n")