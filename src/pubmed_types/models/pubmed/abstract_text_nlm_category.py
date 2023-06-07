from enum import Enum


class AbstractTextNlmCategory(Enum):
    BACKGROUND = "BACKGROUND"
    OBJECTIVE = "OBJECTIVE"
    METHODS = "METHODS"
    RESULTS = "RESULTS"
    CONCLUSIONS = "CONCLUSIONS"
    UNASSIGNED = "UNASSIGNED"
