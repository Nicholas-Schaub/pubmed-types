from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Union
from .access_date import (
    Issue,
    IssuePart,
    IssueTitle,
    Volume,
    VolumeId,
    VolumeSeries,
)
from .issue_id import IssueId
from .issue_sponsor import IssueSponsor
from .issue_title_group import IssueTitleGroup
from .org.w3.xml.pkg_1998.namespace.lang_value import LangValue


@dataclass
class VolumeIssueGroup:
    """
    <div> <h3>Translated Title Group</h3> </div>
    """
    class Meta:
        name = "volume-issue-group"

    volume: List[Volume] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    volume_id: List[VolumeId] = field(
        default_factory=list,
        metadata={
            "name": "volume-id",
            "type": "Element",
        }
    )
    volume_series: Optional[VolumeSeries] = field(
        default=None,
        metadata={
            "name": "volume-series",
            "type": "Element",
        }
    )
    issue: List[Issue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issue_id: List[IssueId] = field(
        default_factory=list,
        metadata={
            "name": "issue-id",
            "type": "Element",
        }
    )
    issue_title: List[IssueTitle] = field(
        default_factory=list,
        metadata={
            "name": "issue-title",
            "type": "Element",
        }
    )
    issue_title_group: List[IssueTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "issue-title-group",
            "type": "Element",
        }
    )
    issue_sponsor: List[IssueSponsor] = field(
        default_factory=list,
        metadata={
            "name": "issue-sponsor",
            "type": "Element",
        }
    )
    issue_part: Optional[IssuePart] = field(
        default=None,
        metadata={
            "name": "issue-part",
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
