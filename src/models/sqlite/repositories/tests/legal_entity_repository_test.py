import pytest

from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.models.sqlite.settings.connection import db_connection_handler

@pytest.mark.skip(reason="Interacao com o banco")
def test_insert_legal_entity():
    faturamento = 70050
    idade = 9
    nome_fantasia = "EMPRESA TESTE4"
    celular = "4444-4444"
    email_corporativo = "empresateste4@teste4.com"
    categoria = "Categoria S"
    saldo = 500003

    repo = LegalEntityRepository(db_connection_handler)
    repo.insert_legal_entity(
        invoicing=faturamento,
        age=idade,
        trade_name=nome_fantasia,
        telephone=celular,
        email=email_corporativo,
        category=categoria,
        balance=saldo
    )

@pytest.mark.skip(reason="Interaction with db")
def test_get_legal_entity():
    repo = LegalEntityRepository(db_connection_handler)
    mock_legal_entity_name = "EMPRESA teste2"
    response = repo.get_legal_entity(mock_legal_entity_name)
    print(response)

@pytest.mark.skip(reason="Interaction with db")
def test_get_legal_entities():
    repo = LegalEntityRepository(db_connection_handler)
    response = repo.get_legal_entities()
    print(response)

#@pytest.mark.skip(reason="Interaction with db")
def test_update_legal_entity_balance():
    repo = LegalEntityRepository(db_connection_handler)
    mock_legal_entity_name = "EMPRESA teste4"
    mock_new_balance = 2221

    repo.update_legal_entity_balance(legal_entity_name=mock_legal_entity_name, new_balance=mock_new_balance)
    response = repo.get_legal_entity(mock_legal_entity_name)

    print(response)