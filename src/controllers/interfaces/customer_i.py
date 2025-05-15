from abc import ABC, abstractmethod
from typing import Dict

class CustomerInterface(ABC):
    @abstractmethod
    def make_withdraw(self, value: float, customer_name: str) -> Dict:
        pass

    @abstractmethod
    def account_statement(self, customer_name: str) -> Dict:
        pass