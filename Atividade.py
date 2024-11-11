tarefas = []

def adicionar_tarefa(tarefa: str) -> None:
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Parâmetros:
       A tarefa (str): A descrição da tarefa a ser adicionada.
    """
    tarefas.append({"descricao": tarefa, "concluida": False})
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')

def listar_tarefas() -> None:
    """
    Exibe todas as tarefas, indicando se estão concluídas ou não.
    """
    if not tarefas:
        print("Não há tarefas para exibir.")
        return

    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - {status}")

def marcar_concluida(indice: int) -> bool:
    """
    Marca uma tarefa como concluída com base no índice fornecido.

    Parâmetros:
        indice (int): O índice da tarefa a ser marcada como concluída.

    Retorno:
        booleano: True se a tarefa foi marcada com sucesso, False caso contrário.
    """
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print(f'Tarefa "{tarefas[indice]["descricao"]}" marcada como concluída.')
        return True
    else:
        print("Índice inválido. Tente novamente.")
        return False

def remover_tarefa(indice: int) -> bool:
    """
    Remove uma tarefa da lista com base no índice fornecido.

    Parâmetros:
        indice (int): O índice da tarefa a ser removida.

    Retorno:
        booleano: True se a tarefa foi removida com sucesso, False caso contrário.
    """
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f'Tarefa "{tarefa_removida["descricao"]}" removida com sucesso.')
        return True
    else:
        print("Índice inválido. Tente novamente.")
        return False

def exibir_menu() -> None:
    """
    Exibe o menu de opções do sistema de gerenciamento de tarefas.
    """
    print("\nMenu de Opções:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa a marcar como concluída: ")) - 1
            marcar_concluida(indice)
        except ValueError:
            print("Por favor, insira um número válido.")
    elif opcao == "4":
        listar_tarefas()
        try:
            indice = int(input("Digite o número da tarefa a remover: ")) - 1
            remover_tarefa(indice)
        except ValueError:
            print("Por favor, insira um número válido.")
    elif opcao == "5":
        print("Saindo do sistema de gerenciamento de tarefas.")
        break
    else:
        print("Opção inválida. Tente novamente.")