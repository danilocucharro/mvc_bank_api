from src.controllers.interfaces.legal_entity_finder_controller_i import LegalEntityFinderInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class LegalEntityFinderView(ViewInterface):
    def __init__(self, controller: LegalEntityFinderInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_name = http_request.param["legal_entity_name"]
        body_response = self.__controller.find(legal_entity_name)

        return HttpResponse(body=body_response, status_code=200)