from typing import Dict

from src.controllers.interfaces.customer_i import CustomerInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository_i import LegalEntityRepositoryI


class LegalEntityWithdrawController(CustomerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryI):
        self.__legal_entity_repository = legal_entity_repository
        self.__new_balance = None

    def make_withdraw(self, value: float, customer_name: str) -> Dict:
        legal_entity = self.__get_legal_entity_in_db(customer_name)
        self.__validate_withdraw(
            withdraw_amount=value,
            account_balance=legal_entity.saldo
        )
        self.__new_balance = (legal_entity.saldo - value)
        self.__update_balance_in_db(
            legal_entity_name=customer_name,
            new_balance=self.__new_balance
        )
        response = self.__format_response_to_withdraw()

        return response

    def __validate_withdraw(self, withdraw_amount: float, account_balance: float) -> None:
        if withdraw_amount > account_balance:
            raise Exception()

        if withdraw_amount > 50000:
            raise Exception()

    def __get_legal_entity_in_db(self, legal_entity_name: str) -> LegalEntityTable:
        legal_entity = self.__legal_entity_repository.get_legal_entity(legal_entity_name)

        return legal_entity

    def __update_balance_in_db(self, new_balance: float, legal_entity_name: str) -> None:
        self.__legal_entity_repository.update_legal_entity_balance(
            new_balance=new_balance,
            legal_entity_name=legal_entity_name
        )

    def account_statement(self, customer_name: str) -> Dict:
        legal_entity = self.__get_legal_entity_in_db(customer_name)
        response = self.__format_response_to_account_statement(legal_entity.saldo)

        return response

    def __format_response_to_withdraw(self) -> Dict:
        response =  {
            "data": {
                "type": "Withdraw",
                "count": 1,
                "attributes": {
                    "account_statement": {
                        "balance": self.__new_balance
                    }
                }
            }
        }

        return response

    def __format_response_to_account_statement(self, balance: float) -> Dict:
        response = {
            "data": {
                "type": "Account Statement",
                "count": 1,
                "attributes": {
                    "balance": balance
                }
            }
        }

        return response