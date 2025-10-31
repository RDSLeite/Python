def adicionar(inv):
    nome = input("Nome do produto: ")
    if nome in inv.keys():
        print("Produto ja pertence ao inventario")
        return inv
    inv[nome] = {}
    inv[nome]['qtde'] = int(input("Quantidade do produto: "))
    inv[nome]['preço'] = int(input("Preço do produto: "))
    return inv
def atualizar(inv, qt):
    produto = input("Nome do produto a atualizar: ")
    if produto not in inv.keys():
        print("Produto não pertence ao inventario")
        return inv
    inv[produto]['qtde'] = qt
    return inv
def remover(inv):
    produto = input("Nome do produto a remover: ")
    if produto not in inv.keys():
        print("Produto não pertence ao inventario")
        return inv
    del inv[produto]
    return inv
def abaixo_do_stock(inv,qt):
    for produto, dados in inv.items():
        if dados['qtde'] < qt:
            print(produto)         
def valor_total(inv):
    total = 0
    for dados in inv.values():
        total += dados['qtde'] * dados['preço']
    return total