from ..legal_entity_creator_validator import legal_entity_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_legal_entity_creator_validator():
    request = MockRequest({
        "invoicing": 100000,
        "trade_name": "danilo informatica",
        "age": 1,
        "telephone": "1111-1111",
        "email": "daniloinfo@email.com",
        "category": "categoria a",
        "balance": 50000,
    })

    legal_entity_creator_validator(request)