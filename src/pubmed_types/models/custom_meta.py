from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional, Union
from .meta_name import MetaName
from .meta_value import MetaValue
from .org.w3.pkg_1999.xlink.actuate_value import ActuateValue
from .org.w3.pkg_1999.xlink.show_value import ShowValue
from .org.w3.pkg_1999.xlink.type_value import TypeValue
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class CustomMeta:
    """
    <div> <h3>Custom Metadata</h3> </div>
    """
    class Meta:
        name = "custom-meta"

    meta_name: Optional[MetaName] = field(
        default=None,
        metadata={
            "name": "meta-name",
            "type": "Element",
            "required": True,
        }
    )
    meta_value: Optional[MetaValue] = field(
        default=None,
        metadata={
            "name": "meta-value",
            "type": "Element",
            "required": True,
        }
    )
    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
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
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        }
    )
    vocab_term: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        }
    )
    vocab_term_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
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
    type: TypeValue = field(
        init=False,
        default=TypeValue.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
