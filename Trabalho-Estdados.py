tarefas = []
estados = []

def adicionar_tarefa(nome):
    tarefas.append(nome)
    estados.append("pendente")
    print(f"Tarefa '{nome}' adicionada com sucesso.")

def marcar_como_concluida(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        estados[indice] = "concluída"
        print(f"Tarefa '{nome}' marcada como concluída.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        tarefas.pop(indice)
        estados.pop(indice)
        print(f"Tarefa '{nome}' removida com sucesso.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def listar_tarefas():
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"- {tarefa} ({estados[i]})")

def listar_por_estado(estado):
    print(f"Tarefas ({estado}):")
    for i, tarefa in enumerate(tarefas):
        if estados[i] == estado:
            print(f"- {tarefa}")

def pesquisar_tarefa(nome):
    if nome in tarefas:
        indice = tarefas.index(nome)
        print(f"Tarefa encontrada: {tarefas[indice]} ({estados[indice]})")
    else:
        print(f"Tarefa '{nome}' não encontrada.")
