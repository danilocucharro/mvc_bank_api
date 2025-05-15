from src.controllers.interfaces.legal_entity_list_controller_i import LegalEntityListInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository_i import LegalEntityRepositoryI
from typing import Dict, List

class LegalEntityListController(LegalEntityListInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryI):
        self.__legal_entity_repository = legal_entity_repository

    def list(self) -> Dict:
        legal_entities = self.__get_legal_entities_in_db()
        response = self.__format_response(legal_entities)

        return response

    def __get_legal_entities_in_db(self) -> List[LegalEntityTable]:
        legal_entities = self.__legal_entity_repository.get_legal_entities()
        return legal_entities

    def __format_response(self, legal_entities: List[LegalEntityTable]) -> Dict:
        formatted_legal_entities = []

        for legal_entity in legal_entities:
            formatted_legal_entities.append({
                "invoicing": legal_entity.faturamento,
                "age": legal_entity.idade,
                "trade_name": legal_entity.nome_fantasia,
                "telephone": legal_entity.celular,
                "email": legal_entity.email_corporativo,
                "category": legal_entity.categoria,
                "balance": legal_entity.saldo
            })

        return {
            "data": {
                "type": "Legal Entity",
                "count": len(formatted_legal_entities),
                "attributes": formatted_legal_entities
            }
        }
