from src.controllers.interfaces.legal_entity_creator_controller_i import LegalEntityCreatorInterface
from src.models.sqlite.interfaces.legal_entity_repository_i import LegalEntityRepositoryI
from typing import Dict

class LegalEntityCreatorController(LegalEntityCreatorInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryI) -> None:
        self.__legal_entity_repository = legal_entity_repository

    def create(self, legal_entity_data: Dict):
        self.__insert_legal_entity_in_db(
            invoicing=legal_entity_data["invoicing"],
            age=legal_entity_data["age"],
            trade_name=legal_entity_data["trade_name"],
            telephone=legal_entity_data["telephone"],
            email=legal_entity_data["email"],
            category=legal_entity_data["category"],
            balance=legal_entity_data["balance"]
        )
        formatted_response = self.__format_response(legal_entity_data)

        return formatted_response

    def __insert_legal_entity_in_db(
            self,
            invoicing: float,
            age: int,
            trade_name: str,
            telephone: str,
            email: str,
            category: str,
            balance: float
    ) -> None:
        self.__legal_entity_repository.insert_legal_entity(
            invoicing=invoicing,
            age=age,
            trade_name=trade_name,
            telephone=telephone,
            email=email,
            category=category,
            balance=balance
        )

    def __format_response(self, legal_entity_data: Dict) -> Dict:
        return {
            "data": {
                "type": "Legal Entity",
                "count": 1,
                "attributes": legal_entity_data
            }
        }