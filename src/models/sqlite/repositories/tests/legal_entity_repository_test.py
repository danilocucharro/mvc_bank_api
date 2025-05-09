import pytest

from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.models.sqlite.settings.connection import db_connection_handler

@pytest.mark.skip(reason="Interacao com o banco")
def test_insert_legal_entity():
    faturamento = 20000
    idade = 2
    nome_fantasia = "EMPRESA TESTE2"
    celular = "1111-9999"
    email_corporativo = "empresateste2@teste2.com"
    categoria = "Categoria B"
    saldo = 100000

    repo = LegalEntityRepository(db_connection_handler)
    repo.insert_legal_entity(
        faturamento=faturamento,
        idade=idade,
        nome_fantasia=nome_fantasia,
        celular=celular,
        email_corporativo=email_corporativo,
        categoria=categoria,
        saldo=saldo
    )

@pytest.mark.skip(reason="Interaction with db")
def test_get_legal_entity():
    repo = LegalEntityRepository(db_connection_handler)
    mock_legal_entity_name = "EMPRESA TESTE2"
    response = repo.get_legal_entity(mock_legal_entity_name)
    print(response)

@pytest.mark.skip(reason="Interaction with db")
def test_get_legal_entities():
    repo = LegalEntityRepository(db_connection_handler)
    response = repo.get_legal_entities()
    print(response)

def test_update_legal_entity_balance():
    repo = LegalEntityRepository(db_connection_handler)
    mock_legal_entity_name = "EMPRESA TESTE2"
    mock_new_balance = 50

    repo.update_legal_entity_balance(legal_entity_name=mock_legal_entity_name, new_balance=mock_new_balance)
    response = repo.get_legal_entity(mock_legal_entity_name)

    print(response)