from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .custom_meta_group import CustomMetaGroup
from .extended_by import ExtendedBy
from .processing_meta_base_tagset import ProcessingMetaBaseTagset
from .processing_meta_mathml_version import ProcessingMetaMathmlVersion
from .processing_meta_table_model import ProcessingMetaTableModel
from .processing_meta_tagset_family import ProcessingMetaTagsetFamily
from .restricted_by import RestrictedBy


@dataclass
class ProcessingMeta:
    """
    <div> <h3>Processing Metadata Model</h3> </div>
    """
    class Meta:
        name = "processing-meta"

    restricted_by: List[RestrictedBy] = field(
        default_factory=list,
        metadata={
            "name": "restricted-by",
            "type": "Element",
        }
    )
    extended_by: List[ExtendedBy] = field(
        default_factory=list,
        metadata={
            "name": "extended-by",
            "type": "Element",
        }
    )
    custom_meta_group: List[CustomMetaGroup] = field(
        default_factory=list,
        metadata={
            "name": "custom-meta-group",
            "type": "Element",
        }
    )
    base_tagset: Optional[ProcessingMetaBaseTagset] = field(
        default=None,
        metadata={
            "name": "base-tagset",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    math_representation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "math-representation",
            "type": "Attribute",
            "tokens": True,
        }
    )
    mathml_version: Optional[ProcessingMetaMathmlVersion] = field(
        default=None,
        metadata={
            "name": "mathml-version",
            "type": "Attribute",
        }
    )
    table_model: Optional[ProcessingMetaTableModel] = field(
        default=None,
        metadata={
            "name": "table-model",
            "type": "Attribute",
        }
    )
    tagset_family: Optional[ProcessingMetaTagsetFamily] = field(
        default=None,
        metadata={
            "name": "tagset-family",
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
