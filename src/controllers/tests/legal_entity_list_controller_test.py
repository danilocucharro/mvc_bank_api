from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.controllers.legal_entity.legal_entity_list_controller import LegalEntityListController

class MockLegalEntityRepository:
    def get_legal_entities(self):
        return[
            LegalEntityTable(faturamento=20000, idade=2, nome_fantasia="Mario mercado", celular="1234-5678", email_corporativo="mariomercado@email.com", categoria="Categoria C", saldo=125000),
            LegalEntityTable(faturamento=62000, idade=21, nome_fantasia="Patrick Informatica", celular="8765-4321", email_corporativo="patrickinfo@email.com", categoria="Categoria B", saldo=81000)
        ]

def test_legal_entity_list_controller():
    controller = LegalEntityListController(MockLegalEntityRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Legal Entity",
            "count": 2,
            "attributes": [
                {"invoicing": 20000, "age": 2, "trade_name": "Mario mercado", "telephone": "1234-5678", "email": "mariomercado@email.com", "category": "Categoria C", "balance": 125000},
                {"invoicing": 62000, "age": 21, "trade_name": "Patrick Informatica", "telephone": "8765-4321", "email": "patrickinfo@email.com", "category": "Categoria B", "balance": 81000}
            ]
        }
    }

    assert response == expected_response
    print()
    print(response)