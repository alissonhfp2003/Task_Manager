from pymongo import MongoClient
from .config import get_database
from .models import Tarefa

class TarefaDAO:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db["tarefas"]

    def criar_tarefa(self, tarefa):
        if not isinstance(tarefa, Tarefa):
            tarefa = Tarefa.from_dict(tarefa)
        result = self.collection.insert_one(tarefa.to_dict())
        return str(result.inserted_id)

    def listar_tarefas(self):
        tarefas = self.collection.find()
        return [Tarefa.from_dict(tarefa) for tarefa in tarefas]

    def atualizar_status_tarefa(self, tarefa_id, novo_status):
        result = self.collection.update_one(
            {"_id": ObjectId(tarefa_id)},
            {"$set": {"status": novo_status}}
        )
        return result.modified_count > 0

    def deletar_tarefa(self, tarefa_id):
        result = self.collection.delete_one({"_id": ObjectId(tarefa_id)})
        return result.deleted_count > 0
