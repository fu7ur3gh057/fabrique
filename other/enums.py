from enum import Enum


class Status(str, Enum):
    CREATED = "CREATED"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"
    EXPIRED = "EXPIRED"

