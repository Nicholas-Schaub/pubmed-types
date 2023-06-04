from enum import Enum


class ArticlePubModel(Enum):
    PRINT = "Print"
    PRINT_ELECTRONIC = "Print-Electronic"
    ELECTRONIC = "Electronic"
    ELECTRONIC_PRINT = "Electronic-Print"
    ELECTRONIC_E_COLLECTION = "Electronic-eCollection"
