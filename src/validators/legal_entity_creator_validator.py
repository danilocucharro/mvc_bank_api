from pydantic import BaseModel, constr, ValidationError

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest


def legal_entity_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        invoicing: float
        age: int
        trade_name: constr(min_length=1)
        telephone: constr(min_length=1)
        email: constr(min_length=1)
        category: constr(min_length=1)
        balance: float

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors())