from tarefa import Tarefa
import os


lista_de_tarefas = []
menu = None

def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    nova_tarefa = Tarefa(titulo, descricao)
    return nova_tarefa

def visualizar_tarefas():
    indice = 0
    if not lista_de_tarefas:
        print("Lista Vazia")
    print("------------ Lista de Tarefas ------------")
    for i in lista_de_tarefas:
        indice += 1
        print(f"Indice: {indice}")
        print(i)
        print("------------------------------------------")

def apagar_tarefa(i):
    tarefa_remover = lista_de_tarefas[i-1]
    lista_de_tarefas.remove(tarefa_remover)

def alterar_tarefas():
    pass


while (menu := input("1- Criar nova tarefas"
                 "\n2- Visualizar tarefas"
                 "\n3- Apagar tarefa"
                 "\n4- Modificar tarefa"
                 "\n5- Sair"
                 "\nDigite a opção que deseja realizar: ")):
    if not menu.isdigit():
        print("Entrada inválida!")
        menu = 0
        os.system("pause")
    else:
        menu = int(menu)
    match menu:
        case 1:
            lista_de_tarefas.append(criar_tarefa())
            print("\nTarefa criada!")
        case 2:
            visualizar_tarefas()
            os.system("pause")
        case 3:
            visualizar_tarefas()
            i = int(input("Qual tarefa deseja remover? "))
            apagar_tarefa(i)
        case 5:
            print("--------FIM--------")
            break

