import pytest
from app.services import TarefaService

@pytest.fixture
def service():
    return TarefaService()

def test_criar_tarefa(service):
    tarefa_id = service.criar_tarefa("Teste", "Descrição de teste", "Pendente")
    assert tarefa_id is not None

def test_listar_tarefas(service):
    tarefas = service.listar_tarefas()
    assert isinstance(tarefas, list)

def test_atualizar_status_tarefa(service):
    tarefa_id = service.criar_tarefa("Teste", "Descrição de teste", "Pendente")
    atualizado = service.atualizar_status_tarefa(tarefa_id, "Concluído")
    assert atualizado is True

def test_deletar_tarefa(service):
    tarefa_id = service.criar_tarefa("Teste", "Descrição de teste", "Pendente")
    deletado = service.deletar_tarefa(tarefa_id)
    assert deletado is True
