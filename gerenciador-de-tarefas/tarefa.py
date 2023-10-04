import datetime


class Tarefa:

    def __init__(self, titulo, descricao, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")

    def __str__(self):
        return f"Titulo: {self.titulo}\nDescricao: {self.descricao}\nStatus: {self.status}\nData: {self.data}"
