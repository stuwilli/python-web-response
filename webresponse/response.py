from webresponse.status import Status
from webresponse.serializer import Serializer
import time


class Response(Serializer):

    def __init__(self, status: Status, data=None,  errors=None):
        self.status_code = status.status_code
        self.message = status.message
        self.data = data
        self.errors = errors
        self.timestamp = time.time_ns()