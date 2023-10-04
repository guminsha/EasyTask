import tarefa

lista_de_tarefas = []
menu = None
tarefa_atual = tarefa

while (menu := input("1- Criar nova tarefas"
                     "\n2- Visualizar tarefas"
                     "\n3- Apagar tarefa"
                     "\n4- Modificar tarefa"
                     "\nDigite a opcao que deseja realizar: ")):

    match menu:
        case "1":
            lista_de_tarefas.append(tarefa_atual.criar_tarefa())
            print("\nTarefa criada!")
        case "2":
            tarefa_atual.visualizar_tarefas(lista_de_tarefas)
        case "3":
            try:
                tarefa_atual.apagar_tarefa(lista_de_tarefas)
            except IndexError as e:
                print("Digite um indice válido!\nRetornando ao Menu inicial")
        case "4":
            try:
                tarefa_atual.alterar_tarefas(lista_de_tarefas)
            except IndexError as e:
                print("Digite um indice válido!\nRetornando ao Menu inicial")
        case _:
            print("Entrada inválida")
            break
