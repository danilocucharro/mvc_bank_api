from src.controllers.interfaces.customer_i import CustomerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class LegalEntityAccountStatementView(ViewInterface):
    def __init__(self, controller: CustomerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        customer_name = http_request.param["customer_name"]
        body_response = self.__controller.account_statement(customer_name)

        return HttpResponse(body=body_response, status_code=200)