import tarefa

lista_de_tarefas = []
menu = None
tarefa_atual = tarefa

while (menu := input("1- Criar nova tarefas"
                     "\n2- Visualizar tarefas"
                     "\n3- Apagar tarefa"
                     "\n4- Modificar tarefa"
                     "\n5- Sair"
                     "\nDigite a opcao que deseja realizar: ")):

    match menu:
        case "1":
            lista_de_tarefas.append(tarefa_atual.criar_tarefa())
        case "2":
            tarefa_atual.visualizar_tarefas(lista_de_tarefas)
        case "3":
            tarefa_atual.apagar_tarefa(lista_de_tarefas)
        case "4":
            tarefa_atual.alterar_tarefas(lista_de_tarefas)
        case "5":
            print("\n------- Programa Finalizado -------\n")
            break
        case _:
            print("Entrada inválida")
            break
