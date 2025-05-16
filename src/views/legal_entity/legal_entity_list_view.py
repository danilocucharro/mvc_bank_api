from src.controllers.interfaces.legal_entity_list_controller_i import LegalEntityListInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class LegalEntityListView(ViewInterface):
    def __init__(self, controller: LegalEntityListInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entities = self.__controller.list()
        body_response = legal_entities

        return HttpResponse(body=body_response, status_code=200)