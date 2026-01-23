import sqlite3
from tarefas import Tarefa

class GestorTarefas:
    def __init__(self):
        self.conexao = sqlite3.connect("tarefas.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                descricao TEXT,
                data_limite TEXT,
                concluida INTEGER
            )
        """)
        self.conexao.commit()

    def adicionar_tarefa(self, titulo, descricao, data_limite):
        self.cursor.execute("""
            INSERT INTO tarefas (titulo, descricao, data_limite, concluida)
            VALUES (?, ?, ?, 0)
        """, (titulo, descricao, data_limite))
        self.conexao.commit()

    def listar_tarefas(self):
        self.cursor.execute("SELECT * FROM tarefas")
        return self.cursor.fetchall()

    def marcar_concluida(self, id_tarefa):
        self.cursor.execute("""
            UPDATE tarefas
            SET concluida = 1
            WHERE id = ?
        """, (id_tarefa,))
        self.conexao.commit()

    def remover_tarefa(self, id_tarefa):
        self.cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()