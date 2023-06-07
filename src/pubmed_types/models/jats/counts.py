from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .count import Count
from .equation_count import EquationCount
from .fig_count import FigCount
from .page_count import PageCount
from .ref_count import RefCount
from .table_count import TableCount
from .word_count import WordCount


@dataclass
class Counts:
    """
    <div> <h3>Counts</h3> </div>
    """
    class Meta:
        name = "counts"

    count: List[Count] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fig_count: Optional[FigCount] = field(
        default=None,
        metadata={
            "name": "fig-count",
            "type": "Element",
        }
    )
    table_count: Optional[TableCount] = field(
        default=None,
        metadata={
            "name": "table-count",
            "type": "Element",
        }
    )
    equation_count: Optional[EquationCount] = field(
        default=None,
        metadata={
            "name": "equation-count",
            "type": "Element",
        }
    )
    ref_count: Optional[RefCount] = field(
        default=None,
        metadata={
            "name": "ref-count",
            "type": "Element",
        }
    )
    page_count: Optional[PageCount] = field(
        default=None,
        metadata={
            "name": "page-count",
            "type": "Element",
        }
    )
    word_count: Optional[WordCount] = field(
        default=None,
        metadata={
            "name": "word-count",
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
