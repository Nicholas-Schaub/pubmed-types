from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional
from .accession_number_list import AccessionNumberList


@dataclass
class DataBank:
    data_bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataBankName",
            "type": "Element",
            "required": True,
        }
    )
    accession_number_list: Optional[AccessionNumberList] = field(
        default=None,
        metadata={
            "name": "AccessionNumberList",
            "type": "Element",
        }
    )
