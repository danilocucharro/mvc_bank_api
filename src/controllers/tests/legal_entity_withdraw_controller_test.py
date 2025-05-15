from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.controllers.legal_entity.legal_entity_withdraw_controller import LegalEntityWithdrawController
import pytest

class MockLegalEntityRepository:
    def get_legal_entity(self, legal_entity_name: str):
        return LegalEntityTable(faturamento=62000, idade=21, nome_fantasia="Patrick Informatica", celular="8765-4321", email_corporativo="patrickinfo@email.com", categoria="Categoria B", saldo=81000)

    def update_legal_entity_balance(self, new_balance: float, legal_entity_name: str):
        pass

def test_legal_entity_withdraw():
    controller = LegalEntityWithdrawController(MockLegalEntityRepository())
    response = controller.make_withdraw(value=20000, customer_name="Patrick Informatica")

    expected_response = {
        "data": {
            "type": "Withdraw",
            "count": 1,
            "attributes": {
                "account_statement": {
                    "balance": 61000
                }
            }
        }
    }

    assert response == expected_response

    print()
    print(response)

def test_legal_entity_withdraw_error():
    controller = LegalEntityWithdrawController(MockLegalEntityRepository())

    with pytest.raises(Exception):
        controller.make_withdraw(value=51000, customer_name="Patrick Informatica")

    response = controller.make_withdraw(value=51000, customer_name="Patrick Informatica")

    print()
    print(response)

def test_legal_entity_account_statement():
    controller = LegalEntityWithdrawController(MockLegalEntityRepository())
    response = controller.account_statement("Patrick Informatica")

    expected_response = {
        "data": {
            "type": "Account Statement",
            "count": 1,
            "attributes": {
                "balance": 81000
            }
        }
    }

    assert response == expected_response

    print()
    print(response)