from src.controllers.legal_entity.legal_entity_creator_controller import LegalEntityCreatorController

class MockLegalEntityRepository:
    def insert_legal_entity(
            self,
            invoicing: float,
            age: int,
            trade_name: str,
            telephone: str,
            email: str,
            category: str,
            balance: float
    ):  pass

def test_create():
    legal_entity_data = {
        "invoicing": 20000,
        "age": 4,
        "trade_name": "EMPRESA4 TESTE",
        "telephone": "2345-0987",
        "email": "empresateste4@teste4.com.br",
        "category": "categoria A",
        "balance": 150000
    }

    controller = LegalEntityCreatorController(MockLegalEntityRepository())

    response = controller.create(legal_entity_data)
    assert response["data"]["type"] == "Legal Entity"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == legal_entity_data

    print()
    print(response)