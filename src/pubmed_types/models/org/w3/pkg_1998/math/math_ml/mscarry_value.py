from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MscarryValue(Enum):
    NONE = "none"
    UPDIAGONALSTRIKE = "updiagonalstrike"
    DOWNDIAGONALSTRIKE = "downdiagonalstrike"
    VERTICALSTRIKE = "verticalstrike"
    HORIZONTALSTRIKE = "horizontalstrike"
