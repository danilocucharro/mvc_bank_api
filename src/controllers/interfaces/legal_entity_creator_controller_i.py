from abc import ABC, abstractmethod
from typing import Dict

class LegalEntityCreatorInterface(ABC):
    @abstractmethod
    def create(self, legal_entity_data: Dict):
        pass