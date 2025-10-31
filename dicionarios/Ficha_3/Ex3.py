biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

for livro in biblioteca.values():
    if livro["disponivel"]:
        print(livro["titulo"])

novo_livro = {
    "titulo": "TITULO novo",
    "autor": "Rui",
    "ano": 2015,
    "disponivel": True
}
biblioteca["livro4"] = novo_livro

biblioteca["livro1"]["disponivel"] = False

def livros_do_autor(autor):
    livros_do_autor = []
    for livro in biblioteca.values():
        if livro['autor'] == autor:
            livros_do_autor.append(livro["titulo"])
    return livros_do_autor