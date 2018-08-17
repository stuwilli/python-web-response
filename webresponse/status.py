from http import HTTPStatus


class Status:

    def __init__(self, code: int):
        self.status_code = code
        self.message = Status.resolve_status_code(code)

    @staticmethod
    def resolve_status_code(code: int) -> str:
        return HTTPStatus(code).name
