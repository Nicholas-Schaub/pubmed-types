from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .type_type import TypeType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class LocatorType:
    """
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar title:
    :ivar label: label is not required, but locators have no particular
        XLink function if they are not labeled.
    """
    class Meta:
        name = "locatorType"

    type: TypeType = field(
        init=False,
        default=TypeType.LOCATOR,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
