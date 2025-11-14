# Importa o módulo json para ler e escrever ficheiros JSON
import json
# Importa o módulo os para verificar a existência de ficheiros
import os


# Caminho para o ficheiro JSON onde o inventário será guardado
FICHEIRO = "ficha4/inventario.json"


# ============================
# 1. CARREGAR E GUARDAR DADOS
# ============================

def carregar_inventario():
    """Carrega o inventário do ficheiro JSON."""

    # Verifica se o ficheiro existe; se não existir, retorna lista vazia
    if not os.path.exists(FICHEIRO):
        return []

    try:
        # Abre o ficheiro JSON em modo leitura
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            # Converte o conteúdo JSON para lista/dicionário Python
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Caso haja erro ao ler o ficheiro, devolve lista vazia
        return []


def guardar_inventario(inventario):
    """Guarda o inventário no ficheiro JSON."""

    # Abre o ficheiro em modo escrita e grava o conteúdo de inventario
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        # json.dump grava no formato JSON com indentação legível
        json.dump(inventario, f, indent=4, ensure_ascii=False)


# ============================
# 2. FUNÇÕES AUXILIARES
# ============================

def gerar_novo_id(inventario):
    """Gera um ID novo baseado nos IDs já existentes."""

    # Se o inventário estiver vazio, começa no ID 1
    if not inventario:
        return 1

    # Encontra o maior ID existente e soma 1
    return max(item["id"] for item in inventario) + 1


def input_inteiro_positivo(mensagem):
    """Pede um inteiro positivo ao utilizador com validação."""

    while True:
        try:
            # Tenta converter a entrada para inteiro
            valor = int(input(mensagem))

            # Se for negativo, mostra erro e repete
            if valor < 0:
                print("O valor deve ser positivo.")
                continue

            return valor

        except ValueError:
            # Caso o input não seja número inteiro
            print("Entrada inválida.")


def input_float_positivo(mensagem):
    """Pede um valor float positivo ao utilizador."""

    while True:
        try:
            # Tenta converter para float
            valor = float(input(mensagem))

            # Não permite números negativos
            if valor < 0:
                print("O valor deve ser positivo.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida.")


def encontrar_item_por_id(inventario, id_item):
    """Procura um item pelo ID e retorna o dicionário correspondente."""

    # Percorre todos os itens do inventário
    for item in inventario:
        # Se o ID coincidir, retorna o item
        if item["id"] == id_item:
            return item

    # Se não encontrar, retorna None
    return None


# ============================
# 3. OPERAÇÕES CRUD
# ============================

def ver_inventario(inventario):
    """Mostra o inventário completo numa tabela formatada."""

    # Se não houver itens, informa o utilizador
    if not inventario:
        print("\nInventário vazio.\n")
        return

    # Cabeçalho formatado da tabela
    print("\n======= INVENTÁRIO =======")
    print(f"{'ID':<5}{'Título':<30}{'Autor':<25}{'Qtd':<5}{'Preço (€)':<10}")
    print("-" * 75)

    # Mostra cada item numa linha organizada
    for item in inventario:
        print(f"{item['id']:<5}{item['titulo']:<30}{item['autor']:<25}{item['quantidade']:<5}{item['preco']:<10.2f}")

    print()


def adicionar_item(inventario):
    """Adiciona um novo livro ao inventário."""

    print("\n--- Adicionar Novo Livro ---")

    # Recolhe os dados do novo livro
    titulo = input("Título: ")
    autor = input("Autor: ")
    quantidade = input_inteiro_positivo("Quantidade: ")
    preco = input_float_positivo("Preço (€): ")

    # Cria o novo dicionário/livro
    novo_item = {
        "id": gerar_novo_id(inventario),  # Gera ID automático
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        "preco": preco
    }

    # Adiciona ao inventário
    inventario.append(novo_item)

    print("Livro adicionado com sucesso!\n")


def atualizar_quantidade(inventario):
    """Atualiza a quantidade de um livro existente."""

    print("\n--- Atualizar Quantidade ---")

    # Pede o ID ao utilizador
    id_item = input_inteiro_positivo("ID do livro: ")

    # Procura o item
    item = encontrar_item_por_id(inventario, id_item)

    # Se não existir, avisa
    if not item:
        print("Item não encontrado.\n")
        return

    # Pede nova quantidade
    nova_quantidade = input_inteiro_positivo("Nova quantidade: ")

    # Atualiza
    item["quantidade"] = nova_quantidade

    print("Quantidade atualizada com sucesso!\n")


def remover_item(inventario):
    """Remove um item do inventário."""

    print("\n--- Remover Item ---")

    # Pede ID ao utilizador
    id_item = input_inteiro_positivo("ID do livro: ")

    # Procura o item
    item = encontrar_item_por_id(inventario, id_item)

    # Se não existir, avisa
    if not item:
        print("Item não encontrado.\n")
        return

    # Remove o item da lista
    inventario.remove(item)

    print("Item removido com sucesso!\n")


def pesquisa_avancada(inventario):
    """Pesquisa por parte do título ou autor."""

    # Termo digitado pelo utilizador convertido para minúsculas
    termo = input("Pesquisar por título ou autor: ").lower()

    # Lista de itens que contêm o termo no título OU autor
    resultados = [
        item for item in inventario
        if termo in item["titulo"].lower() or termo in item["autor"].lower()
    ]

    # Se não encontrar nenhum, avisa
    if not resultados:
        print("Nenhum resultado encontrado.\n")
        return

    print("\nResultados da pesquisa:")
    ver_inventario(resultados)  # Mostra a tabela com resultados


def relatorio_stock(inventario):
    """Calcula e mostra o valor total monetário do inventário."""

    # Soma de quantidade * preço de todos os produtos
    total = sum(item["quantidade"] * item["preco"] for item in inventario)

    print(f"\nValor total do inventário: {total:.2f} €\n")
