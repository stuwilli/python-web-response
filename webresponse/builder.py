from webresponse.response import Response
from webresponse.status import Status


class ResponseBuilder:

    def __init__(self):
        self.status = 200
        self.data = {}
        self.errors = []

    def add_named_error(self, name: str, error: str):
        err = {name: error}
        self.errors.append(err)

    def add_unnamed_error(self, error: str):
        name = "error_" + str(len(self.errors) + 1)
        self.add_named_error(name, error)

    def add_exception(self, e: Exception):
        self.add_unnamed_error(str(e))

    def build(self) -> Response:
        status = Status(self.status)
        resp = Response(status)

        if self.data is not None and len(self.data) > 0:
            resp.data = self.data

        if self.errors is not None and len(self.errors) > 0:
            resp.errors = self.errors

        return resp
