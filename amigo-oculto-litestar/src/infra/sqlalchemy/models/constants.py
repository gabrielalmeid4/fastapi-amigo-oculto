from enum import Enum


class Status(Enum):
    CANCELLED = "CANCELLED"
    CLOSED = "CLOSED"
    ONGOING = "ONGOING"
    OPEN = "OPEN"
