from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List
from .data_bank import DataBank
from .data_bank_list_complete_yn import DataBankListCompleteYn


@dataclass
class DataBankList:
    complete_yn: DataBankListCompleteYn = field(
        default=DataBankListCompleteYn.Y,
        metadata={
            "name": "CompleteYN",
            "type": "Attribute",
            "required": True,
        }
    )
    data_bank: List[DataBank] = field(
        default_factory=list,
        metadata={
            "name": "DataBank",
            "type": "Element",
            "min_occurs": 1,
        }
    )
