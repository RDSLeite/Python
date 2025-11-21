import os, json 
import functions as fnc

caminho = "ficha4/livros.json"
inventario = {}
if not os.path.exists(caminho):
    with open(caminho,"w") as f:
        json.dump({},f,ensure_ascii =False)
else:
    inventario = fnc.carregarInventario(caminho)
    
# title = input("Digite o nome do livro: ")
# author = input("Digite o autor do livro: ")
# quantity = int(input("Digite a quantidade fornecida: "))
# price = float(input("Preço do livro: "))
# inventario = fnc.adicionarItem(inventario,title,author,quantity,price)
# fnc.guardarInventario(caminho,inventario)

id_localizar = int(input("Digite o id do livro a atualizar a quantidade: "))
inventario = fnc.atualizarQuantidade(inventario, id_localizar)
fnc.guardarInventario(caminho,inventario)