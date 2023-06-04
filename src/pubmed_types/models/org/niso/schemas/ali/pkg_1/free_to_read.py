from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.niso.org/schemas/ali/1.0/"


@dataclass
class FreeToRead:
    class Meta:
        name = "free_to_read"
        namespace = "http://www.niso.org/schemas/ali/1.0/"

    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
