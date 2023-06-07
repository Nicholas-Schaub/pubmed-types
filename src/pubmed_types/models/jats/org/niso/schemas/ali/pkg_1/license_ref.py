from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional

__NAMESPACE__ = "http://www.niso.org/schemas/ali/1.0/"


@dataclass
class LicenseRef:
    """
    <div> <h3>License Reference (Niso Ali)</h3> </div>
    """
    class Meta:
        name = "license_ref"
        namespace = "http://www.niso.org/schemas/ali/1.0/"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
