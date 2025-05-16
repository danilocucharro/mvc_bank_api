from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict, param: Dict) -> None:
        self.body = body
        self.param = param