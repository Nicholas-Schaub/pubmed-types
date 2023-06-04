from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.niso.org/schemas/ali/1.0/"


@dataclass
class LicenseRef:
    class Meta:
        name = "license_ref"
        namespace = "http://www.niso.org/schemas/ali/1.0/"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
