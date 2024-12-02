from bson.objectid import ObjectId
from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, status, data_criacao=None, _id=None):
        self._id = _id if _id else ObjectId()
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_criacao = data_criacao if data_criacao else datetime.utcnow()

    def to_dict(self):
        return {
            "_id": self._id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_criacao": self.data_criacao
        }

    @staticmethod
    def from_dict(data):
        return Tarefa(
            titulo=data.get("titulo"),
            descricao=data.get("descricao"),
            status=data.get("status"),
            data_criacao=data.get("data_criacao"),
            _id=data.get("_id")
        )
