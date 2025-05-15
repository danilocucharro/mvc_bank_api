from abc import ABC, abstractmethod
from typing import Dict

class LegalEntityListInterface(ABC):
    @abstractmethod
    def list(self) -> Dict:
        pass