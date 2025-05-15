from abc import ABC, abstractmethod
from typing import Dict

class LegalEntityFinderInterface(ABC):
    @abstractmethod
    def find(self, legal_entity_name: str) -> Dict:
        pass