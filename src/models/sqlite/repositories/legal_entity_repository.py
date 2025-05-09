from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository_interface import LegalEntityRepositoryInterface
from src.models.sqlite.settings.connection import DBConnectionHandler


class LegalEntityRepository(LegalEntityRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_legal_entity(
            self,
            faturamento: int,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: int
    ) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia.lower(),
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
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
            except Exception as exception:
                raise exception
                return []

    def get_legal_entities(self) -> LegalEntityTable:
        with self.__db_connection as database:
            try:
                legal_entities = database.session.query(LegalEntityTable).all()
                return legal_entities
            except Exception as exception:
                raise exception
                return []

    def update_legal_entity_balance(self, legal_entity_name: str, new_balance: int):
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.nome_fantasia == legal_entity_name.lower())
                    .first()
                )
                if not legal_entity:
                    print("Entidade nao encontrada")
                    return

                legal_entity.saldo = new_balance
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
