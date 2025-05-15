from src.controllers.interfaces.legal_entity_finder_controller_i import LegalEntityFinderInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository_i import LegalEntityRepositoryI
from typing import Dict

class LegalEntityFinderController(LegalEntityFinderInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryI):
        self.__legal_entity_repository = legal_entity_repository

    def find(self, legal_entity_name: str) -> Dict:
        legal_entity = self.__get_legal_entity_in_db(legal_entity_name)
        response = self.__format_response(legal_entity)

        return  response

    def __get_legal_entity_in_db(self, legal_entity_name: str) -> LegalEntityTable:
        legal_entity = self.__legal_entity_repository.get_legal_entity(legal_entity_name)

        return legal_entity

    def __format_response(self, legal_entity: LegalEntityTable) -> Dict:
        response = {
            "data": {
                "type": "Legal Entity",
                "count": 1,
                "attributes": [{
                    "invoicing": legal_entity.faturamento,
                    "age": legal_entity.idade,
                    "trade_name": legal_entity.nome_fantasia,
                    "telephone": legal_entity.celular,
                    "email": legal_entity.email_corporativo,
                    "category": legal_entity.categoria,
                    "balance": legal_entity.saldo
                }]
            }
        }

        return response