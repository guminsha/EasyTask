import datetime


class Tarefa:

    def __init__(self, titulo, descricao, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")

    def __str__(self):
        return f"Titulo: {self.titulo}\nDescricao: {self.descricao}\nStatus: {self.status}\nData: {self.data}"


def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    nova_tarefa = Tarefa(titulo, descricao)

    return nova_tarefa


def visualizar_tarefas(lista_de_tarefas):
    indice = 0
    if not lista_de_tarefas:
        print("---- Lista Vazia! ----\n")
        return 0
    print("\n------------ Lista de Tarefas ------------")
    for i in lista_de_tarefas:
        indice += 1
        print(f"Indice: {indice}")
        print(i)
        print("------------------------------------------")



def apagar_tarefa(lista_de_tarefas):
    menu = visualizar_tarefas(lista_de_tarefas)
    if menu == 0:
        return 0
    i = int(input("Qual tarefa deseja remover? "))
    tarefa_remover = lista_de_tarefas[i - 1]
    lista_de_tarefas.remove(tarefa_remover)

def alterar_tarefas(lista_de_tarefas):
    menu = visualizar_tarefas(lista_de_tarefas)
    if menu == 0:
        return 0
    i = int(input("Qual tarefa deseja modificar? "))
    tarefa_alterar = lista_de_tarefas[i - 1]  # aponta para o endereço da memória
    while (menu := input("1- Alterar titulo"
                             "\n2- Alterar descricao"
                             "\n3- Alterar status"
                             "\nDigite a opção que deseja realizar: ")):

        match menu:
            case "1":
                tarefa_alterar.titulo = input("Digite o novo titulo da tarefa: ")
            case "2":
                tarefa_alterar.descricao = input("Digite a nova descricao da tarefa: ")
            case "3":
                if tarefa_alterar.status == "Pendente":
                    tarefa_alterar.status = "Concluida"
                else:
                    tarefa_alterar.status = "Pendente"
            case _:
                print("Entrada inválida")
                break
