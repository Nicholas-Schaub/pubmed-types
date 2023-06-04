from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List


@dataclass
class GeneSymbolList:
    gene_symbol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GeneSymbol",
            "type": "Element",
            "min_occurs": 1,
        }
    )
