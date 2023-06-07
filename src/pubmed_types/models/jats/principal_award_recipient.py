from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    Institution,
    InstitutionWrap,
    Name,
    NameAlternatives,
    StringName,
)
from .contrib_id import ContribId
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class PrincipalAwardRecipient:
    """
    <div> <h3>Principal Award Recipient</h3> </div>
    """
    class Meta:
        name = "principal-award-recipient"

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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "contrib-id",
                    "type": ContribId,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "name-alternatives",
                    "type": NameAlternatives,
                },
                {
                    "name": "institution",
                    "type": Institution,
                },
                {
                    "name": "institution-wrap",
                    "type": InstitutionWrap,
                },
                {
                    "name": "string-name",
                    "type": StringName,
                },
            ),
        }
    )
