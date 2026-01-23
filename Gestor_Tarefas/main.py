from gestor import GestorTarefas

def menu():
    print("\n--- GESTOR DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("0. Sair")

def main():
    gestor = GestorTarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data_limite = input("Data limite (YYYY-MM-DD): ")
            gestor.adicionar_tarefa(titulo, descricao, data_limite)
            print("✅ Tarefa adicionada com sucesso!")

        elif opcao == "2":
            tarefas = gestor.listar_tarefas()
            for t in tarefas:
                estado = "Concluída" if t[4] == 1 else "Pendente"
                print(f"ID: {t[0]} | {t[1]} | {t[2]} | {t[3]} | {estado}")

        elif opcao == "3":
            id_tarefa = int(input("ID da tarefa a concluir: "))
            gestor.marcar_concluida(id_tarefa)
            print("✔️ Tarefa marcada como concluída!")

        elif opcao == "4":
            id_tarefa = int(input("ID da tarefa a remover: "))
            gestor.remover_tarefa(id_tarefa)
            print("🗑️ Tarefa removida!")

        elif opcao == "0":
            gestor.fechar()
            print("👋 A sair...")
            break

        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()