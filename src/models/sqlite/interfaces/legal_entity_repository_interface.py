from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityRepositoryInterface(ABC):

    @abstractmethod
    def insert_legal_entity(
            self,
            faturamento: str,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: int
    ) -> None: pass

    @abstractmethod
    def get_legal_entity(self, legal_entity_id: int) -> LegalEntityTable: pass