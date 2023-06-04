from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .url_lang import UrlLang
from .url_type import UrlType


@dataclass
class Url:
    class Meta:
        name = "URL"

    lang: Optional[UrlLang] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[UrlType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
