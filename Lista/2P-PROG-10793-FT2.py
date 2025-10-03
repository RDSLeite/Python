# Criamos uma lista vazia para armazenar as tarefas
tarefas = []

# 1. Adicionar Tarefa -> usamos append para adicionar uma tarefa no final
tarefas.append("Ir ao cinema")
print("1:", tarefas)

# 2. Adicionar Múltiplas Tarefas -> usamos extend para adicionar várias de uma vez
tarefas.extend(["Lavar roupa", "Secar cabelo"])
print("2:", tarefas)

# 3. Inserir Tarefa em Posição Específica -> insert(posição, tarefa)
tarefas.insert(1, "Estudar Python")  # vai colocar na posição 1
print("3:", tarefas)

# 4. Remover Tarefa por Nome -> remove("nome_da_tarefa")
tarefas.remove("Lavar roupa")  # remove exatamente essa string
print("4:", tarefas)

# 5a. Remover Última Tarefa -> pop() sem nada tira o último
tarefas.pop()
print("5a:", tarefas)

# 5b. Remover Tarefa por Índice -> pop(indice)
tarefas.pop(0)  # tira a primeira tarefa (posição 0)
print("5b:", tarefas)

# 6. Remover todas as Tarefas -> clear() esvazia a lista
tarefas.clear()
print("6:", tarefas)

# Criamos de novo algumas tarefas para continuar os exemplos
tarefas = ["Ir ao cinema", "Estudar Python", "Ir ao cinema", "Dormir"]

# 7. Contar Ocorrências -> count("nome_da_tarefa") conta quantas vezes aparece
print("7: 'Ir ao cinema' aparece", tarefas.count("Ir ao cinema"), "vezes")

# 8. Encontrar Índice -> index("nome_da_tarefa") mostra a posição da primeira vez que aparece
print("8: 'Dormir' está na posição", tarefas.index("Dormir"))

# 9. Ordenar Tarefas -> sort() coloca em ordem alfabética
tarefas.sort()
print("9:", tarefas)

# 10. Inverter Ordem -> reverse() deixa a lista de trás para frente
tarefas.reverse()
print("10:", tarefas)

# 11. Copiar Lista -> copy() cria uma cópia independente
tarefas2 = tarefas.copy()
print("11: Cópia ->", tarefas2)
