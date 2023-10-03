from tarefa import Tarefa

lista_de_tarefas = []

def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    nova_tarefa = Tarefa(titulo, descricao)
    return nova_tarefa

def visualizar_tarefas():
    for i in lista_de_tarefas:
        print(i)


def apagar_tarefa():
    pass


def alterar_tarefas():
    pass


while True:
    lista_de_tarefas.append(criar_tarefa())
    print("\nTarefa criada!")

    if(input("Nova tarefa?(S/N) ").upper()) == "N":
        break
