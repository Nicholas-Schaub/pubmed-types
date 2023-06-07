from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import IssueTitle
from .issue_subtitle import IssueSubtitle
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue
from .trans_title_group import TransTitleGroup


@dataclass
class IssueTitleGroup:
    """
    <div> <h3>Issue Title Group</h3> </div>
    """
    class Meta:
        name = "issue-title-group"

    issue_title: Optional[IssueTitle] = field(
        default=None,
        metadata={
            "name": "issue-title",
            "type": "Element",
            "required": True,
        }
    )
    issue_subtitle: List[IssueSubtitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-subtitle",
            "type": "Element",
        }
    )
    trans_title_group: List[TransTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "trans-title-group",
            "type": "Element",
        }
    )
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
