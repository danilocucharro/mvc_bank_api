from src.controllers.legal_entity.legal_entity_finder_controller import LegalEntityFinderController
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.views.legal_entity.legal_entity_finder_view import LegalEntityFinderView

def legal_entity_finder_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityFinderController(model)
    view = LegalEntityFinderView(controller)

    return view