from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class GlyphRef:
    """
    <div> <h3>Glyph Reference For a Private Character</h3> </div>
    """
    class Meta:
        name = "glyph-ref"

    glyph_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "glyph-data",
            "type": "Attribute",
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
