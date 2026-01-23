class Tarefa:
    def __init__(self,titulo, descricao, data_limite, concluida):
        self._titulo = titulo
        self._descricao = descricao
        self._data_limite = data_limite
        self._concluida = False

    # Getters

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_data_limite(self):
        return self._data_limite

    def get_concluida(self):
        return self._concluida

    # Setters (apenas os necessários)
    def set_concluida(self, concluida):
        self._concluida = concluida