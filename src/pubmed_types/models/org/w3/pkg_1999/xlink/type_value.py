from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class TypeValue(Enum):
    SIMPLE = "simple"
    EXTENDED = "extended"
    LOCATOR = "locator"
    ARC = "arc"
    RESOURCE = "resource"
    TITLE = "title"
    NONE = "none"
