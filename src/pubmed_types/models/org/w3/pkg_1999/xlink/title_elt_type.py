from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .type_value import TypeValue
from ...xml.pkg_1998.namespace.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass
class TitleEltType:
    """
    :ivar type:
    :ivar lang: xml:lang is not required, but provides much of the
        motivation for title elements in addition to attributes, and so
        is provided here for convenience.
    :ivar content:
    """
    class Meta:
        name = "titleEltType"

    type: TypeValue = field(
        init=False,
        default=TypeValue.TITLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
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
