from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .access_date import (
    Aff,
    AffAlternatives,
    ContribGroup,
    Isbn,
    Issn,
    IssnL,
    Notes,
)
from .custom_meta_group import CustomMetaGroup
from .journal_id import JournalId
from .journal_title_group import JournalTitleGroup
from .publisher_2 import Publisher2
from .self_uri import SelfUri


@dataclass
class JournalMeta:
    """
    <div> <h3>Journal Metadata</h3> </div>
    """
    class Meta:
        name = "journal-meta"

    journal_id: List[JournalId] = field(
        default_factory=list,
        metadata={
            "name": "journal-id",
            "type": "Element",
        }
    )
    journal_title_group: List[JournalTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "journal-title-group",
            "type": "Element",
        }
    )
    contrib_group: List[ContribGroup] = field(
        default_factory=list,
        metadata={
            "name": "contrib-group",
            "type": "Element",
        }
    )
    aff: List[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    aff_alternatives: List[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
        }
    )
    issn: List[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issn_l: Optional[IssnL] = field(
        default=None,
        metadata={
            "name": "issn-l",
            "type": "Element",
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    publisher: Optional[Publisher2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    notes: List[Notes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    self_uri: List[SelfUri] = field(
        default_factory=list,
        metadata={
            "name": "self-uri",
            "type": "Element",
        }
    )
    custom_meta_group: Optional[CustomMetaGroup] = field(
        default=None,
        metadata={
            "name": "custom-meta-group",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
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
