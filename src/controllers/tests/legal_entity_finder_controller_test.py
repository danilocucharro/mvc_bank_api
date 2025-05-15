from src.controllers.legal_entity.legal_entity_finder_controller import LegalEntityFinderController
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.controllers.legal_entity.legal_entity_list_controller import LegalEntityListController

class MockLegalEntityRepository:
    def get_legal_entity(self, legal_entity_name: str):
        return LegalEntityTable(faturamento=20000, idade=2, nome_fantasia="Mario mercado", celular="1234-5678", email_corporativo="mariomercado@email.com", categoria="Categoria C", saldo=125000)

def test_legal_entity_finder_controller():
    controller = LegalEntityFinderController(MockLegalEntityRepository())
    response = controller.find("mario mercado")

    expected_response = {
        "data": {
            "type": "Legal Entity",
            "count": 1,
            "attributes": [
                {"invoicing": 20000, "age": 2, "trade_name": "Mario mercado", "telephone": "1234-5678", "email": "mariomercado@email.com", "category": "Categoria C", "balance": 125000},
            ]
        }
    }

    assert response == expected_response
    print()
    print(response)