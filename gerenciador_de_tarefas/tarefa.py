import datetime
import indice_invalido_exception


class Tarefa:

    def __init__(self, titulo, descricao, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")

    def __str__(self):
        return f"Titulo: {self.titulo}\nDescricao: {self.descricao}\nStatus: {self.status}\nData: {self.data}"


def criar_tarefa():
    titulo = input("Digite o titulo da tarefa: ")
    descricao = input("Digite a descricao da tarefa: ")
    nova_tarefa = Tarefa(titulo, descricao)
    print("\nTarefa criada!\n")

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
    try:
        i = input("Qual tarefa deseja remover? ")
        if not i.isdigit():
            raise indice_invalido_exception.IndiceInvalidoException(
                "Digite um indice valido!\nRetornando ao Menu inicial")
        i = int(i)
        if i < 1 or i > len(lista_de_tarefas):
            raise indice_invalido_exception.IndiceInvalidoException(
                "Digite um indice valido!\nRetornando ao Menu inicial")

        tarefa_remover = lista_de_tarefas[i - 1]  # aponta para o endereço da memória
        print(f"\nTarefa {tarefa_remover.titulo} removida com sucesso!\n")
        lista_de_tarefas.remove(tarefa_remover)
    except indice_invalido_exception.IndiceInvalidoException as e:
        print(e)


def alterar_tarefas(lista_de_tarefas):
    menu = visualizar_tarefas(lista_de_tarefas)
    if menu == 0:
        return 0

    try:
        i = input("Qual tarefa deseja modificar? ")
        if not i.isdigit():
            raise indice_invalido_exception.IndiceInvalidoException(
                "Digite um indice valido!\nRetornando ao Menu inicial")
        i = int(i)
        if i < 1 or i > len(lista_de_tarefas):
            raise indice_invalido_exception.IndiceInvalidoException(
                "Digite um indice valido!\nRetornando ao Menu inicial")

        tarefa_alterar = lista_de_tarefas[i - 1]  # aponta para o endereço da memória
        while (menu := input("1- Alterar titulo"
                             "\n2- Alterar descricao"
                             "\n3- Alterar status"
                             "\n4- Sair"
                             "\nDigite a opcao que deseja realizar: ")):
            match menu:
                case "1":
                    alterar_titulo(tarefa_alterar)
                case "2":
                    alterar_descricao(tarefa_alterar)
                case "3":
                    alterar_status(tarefa_alterar)
                case "4":
                    break
                case _:
                    print("Entrada inválida")
                    break
    except indice_invalido_exception.IndiceInvalidoException as e:
        print(e)


def alterar_titulo(tarefa_alterar):
    tarefa_alterar.titulo = input("Digite o novo titulo da tarefa: ")
    print("titulo alterado com sucesso!\n")


def alterar_descricao(tarefa_alterar):
    tarefa_alterar.descricao = input("Digite a nova descricao da tarefa: ")
    print("Descricao alterada com sucesso!\n")


def alterar_status(tarefa_alterar):
    if tarefa_alterar.status == "Pendente":
        tarefa_alterar.status = "Concluida"
        print("Tarefa alterada para Concluida!\n")
    else:
        tarefa_alterar.status = "Pendente"
        print("Tarefa alterada para Pendente!\n")
