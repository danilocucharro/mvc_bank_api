from src.controllers.legal_entity.legal_entity_list_controller import LegalEntityListController
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.views.legal_entity.legal_entity_list_view import LegalEntityListView

def legal_entity_list_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityListController(model)
    view = LegalEntityListView(controller)

    return view