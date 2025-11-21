import json, os
from datetime import datetime

caminho_log = "ficha4/log.txt"

def carregarInventario(ficheiro):
    d = {}
    with open(ficheiro, "r", encoding="utf-8") as f:
        d = json.load(f)
        print("Livros carregados com sucesso!")
    return d

def guardarInventario(ficheiro, inventario):
    with open(ficheiro, "w", encoding="utf-8")as f:
        json.dump(inventario,f,ensure_ascii=False,indent=4)
        
def escrever_log(msg):
    with open(caminho_log,"a", encoding="utf-8")as f:
        f.write(msg)
        f.write("\n")
        
def adicionarItem(inventario,titulo,autor,qtde,preco):
    if len(inventario) == 0:
        id  = 1
    else:
        id = len(inventario) + 1 
    inventario[str(id)] = {}
    inventario[str(id)]["titulo"] = titulo
    inventario[str(id)]["autor"] = autor
    inventario[str(id)]["quantidade"] = qtde
    inventario[str(id)]["preco"] = preco
    msg = f"O livro {titulo} foi adicionado ao inventario às {datetime.today()}"
    escrever_log(msg)
    return inventario

def atualizarQuantidade(inventario, id):
    if len(inventario) == 0 or id <= len(inventario):
        print("Id invalido")
        return inventario
    qtde = input("Digite a nova quantidade em stock: ")
    inventario[str(id)]["quantidade"] = qtde
    msg = f"A quantidade do livro com id {id} foi atualizada para {qtde} as {datetime.today()}"
    escrever_log(msg)
    return inventario
