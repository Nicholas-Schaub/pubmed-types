from dataclasses import field
from pydantic.dataclasses import dataclass
from .first_page_lzero import FirstPageLzero


@dataclass
class FirstPage:
    lzero: FirstPageLzero = field(
        default=FirstPageLzero.DELETE,
        metadata={
            "name": "LZero",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
