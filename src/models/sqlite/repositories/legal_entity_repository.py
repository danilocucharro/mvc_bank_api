from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository_i import LegalEntityRepositoryI
from src.models.sqlite.settings.connection import DBConnectionHandler
from typing import Dict

class LegalEntityRepository(LegalEntityRepositoryI):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_legal_entity(
            self,
            invoicing: int,
            age: int,
            trade_name: str,
            telephone: str,
            email: str,
            category: str,
            balance: int
    ) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    faturamento=invoicing,
                    idade=age,
                    nome_fantasia=trade_name.lower(),
                    celular=telephone,
                    email_corporativo=email,
                    categoria=category,
                    saldo=balance
                )
                database.session.add(legal_entity_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_legal_entity(self, legal_entity_name: str) -> LegalEntityTable:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database
                    .session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.nome_fantasia == legal_entity_name.lower())
                    .one()
                )
                return legal_entity
            except NoResultFound:
                return None

    def get_legal_entities(self) -> Dict:
        with self.__db_connection as database:
            try:
                legal_entities = database.session.query(LegalEntityTable).all()
                return legal_entities
            except NoResultFound:
                return None

    def update_legal_entity_balance(self, legal_entity_name: str, new_balance: float) -> None:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database
                    .session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.nome_fantasia == legal_entity_name.lower())
                    .one()
                )

                legal_entity.saldo = new_balance
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
