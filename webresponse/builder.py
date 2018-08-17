from webresponse.response import Response
from webresponse.status import Status


class ResponseError:

    def __init__(self, key: str, val: str):
        self.key = key
        self.error = val

    def serialize(self, **kwargs) -> dict:
        return {self.key: self.error}


class ResponseBuilder:

    def __init__(self):
        self.status = 200
        self.data = {}
        self.errors = []

    def add_named_error(self, name: str, error: str):
        err = ResponseError(name, error)
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
            resp.errors = []
            for i in range(len(self.errors)):
                if isinstance(self.errors[i], ResponseError):
                    resp.errors.append(self.errors[i].serialize())

        return resp
