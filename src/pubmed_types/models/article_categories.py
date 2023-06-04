from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .access_date import SubjGroup
from .series_text import SeriesText
from .series_title import SeriesTitle


@dataclass
class ArticleCategories:
    """
    <div> <h3>Article Grouping Data</h3> </div>
    """
    class Meta:
        name = "article-categories"

    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        }
    )
    series_title: List[SeriesTitle] = field(
        default_factory=list,
        metadata={
            "name": "series-title",
            "type": "Element",
        }
    )
    series_text: List[SeriesText] = field(
        default_factory=list,
        metadata={
            "name": "series-text",
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
