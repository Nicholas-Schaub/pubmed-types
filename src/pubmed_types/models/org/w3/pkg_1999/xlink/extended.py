from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .type_value import TypeValue

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class Extended:
    """Intended for use as the type of user-declared elements to make them extended
    links.

    Note that the elements referenced in the content model are all
    abstract. The intention is that by simply declaring elements with
    these as their substitutionGroup, all the right things will happen.
    """
    class Meta:
        name = "extended"

    type: TypeValue = field(
        init=False,
        default=TypeValue.EXTENDED,
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
