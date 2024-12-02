import pytest
from app.dao import TarefaDAO
from app.models import Tarefa

@pytest.fixture
def dao():
    return TarefaDAO()

def test_criar_tarefa(dao):
    tarefa = Tarefa("Teste", "Descrição de teste", "Pendente")
    tarefa_id = dao.criar_tarefa(tarefa)
    assert tarefa_id is not None

def test_listar_tarefas(dao):
    tarefas = dao.listar_tarefas()
    assert isinstance(tarefas, list)

def test_atualizar_status_tarefa(dao):
    tarefa = Tarefa("Teste", "Descrição de teste", "Pendente")
    tarefa_id = dao.criar_tarefa(tarefa)
    atualizado = dao.atualizar_status_tarefa(tarefa_id, "Concluído")
    assert atualizado is True

def test_deletar_tarefa(dao):
    tarefa = Tarefa("Teste", "Descrição de teste", "Pendente")
    tarefa_id = dao.criar_tarefa(tarefa)
    deletado = dao.deletar_tarefa(tarefa_id)
    assert deletado is True
