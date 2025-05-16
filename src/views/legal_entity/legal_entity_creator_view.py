from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from ..interfaces.view_interface import ViewInterface
from src.controllers.interfaces.legal_entity_creator_controller_i import LegalEntityCreatorInterface

class LegalEntityCreatorView(ViewInterface):
    def __init__(self, controller: LegalEntityCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_data = http_request.body
        body_response = self.__controller.create(legal_entity_data)

        return HttpResponse(status_code=201, body=body_response)