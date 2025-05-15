from abc import ABC, abstractmethod

from src.models.sqlite.entities.legal_entity import LegalEntityTable


class LegalEntityRepositoryI(ABC):
    @abstractmethod
    def insert_legal_entity(
            self,
            invoicing: float,
            age: int,
            trade_name: str,
            telephone: str,
            email: str,
            category: str,
            balance: float
    ) -> None: pass

    @abstractmethod
    def get_legal_entity(self, legal_entity_name: str) -> LegalEntityTable: pass

    @abstractmethod
    def get_legal_entities(self) -> LegalEntityTable: pass

    @abstractmethod
    def update_legal_entity_balance(self, legal_entity_name: str, new_balance: float) -> None: pass