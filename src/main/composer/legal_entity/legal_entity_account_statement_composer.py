from src.controllers.legal_entity.legal_entity_withdraw_controller import LegalEntityWithdrawController
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.views.legal_entity.legal_entity_account_statement_view import LegalEntityAccountStatementView


def legal_entity_account_statement_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityWithdrawController(model)
    view = LegalEntityAccountStatementView(controller)

    return view