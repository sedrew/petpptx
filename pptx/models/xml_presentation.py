from dataclasses import dataclass, field
from typing import Optional

from pptx.models.abstract_dataclass import AbstractModel
from pptx.models.name_space import NameSpaces
from pptx.models.xml_default_text_style import DefaultTextStyle


@dataclass
class XmlSlide:
    slide_id: int = field(metadata=dict(type="Attribute", name="id"))
    r_id: str = field(
        metadata=dict(
            name="id",
            namespace=NameSpaces.source_relationship,
            type="Attribute"
        )
    )


@dataclass
class XmlSlides:
    slide: Optional[XmlSlide] = field(
        default=None,
        metadata=dict(
            name="sldId",
            type="Element"
        )
    )


@dataclass
class XmlSlideSize:
    cx: int = field(
        default=12192000,
        metadata=dict(
            name="cx",
            type="Attribute"
        )
    )
    cy: int = field(
        default=6858000,
        metadata=dict(
            name="cy",
            type="Attribute"
        )
    )


@dataclass
class XmlNotesSize:
    cx: int = field(
        default=6858000,
        metadata={
            "name": "cx",
            "type": "Attribute"
        }
    )
    cy: int = field(
        default=9144000,
        metadata={
            "name": "cy",
            "type": "Attribute"
        }
    )


@dataclass
class SlideMaster:
    slide_id: int = field(
        metadata={
            "name": "id",
            "type": "Attribute"
        }
    )
    r_id: str = field(
        metadata={
            "name": "id",
            "type": "Attribute",
            "namespace": NameSpaces.source_relationship,
        }
    )


@dataclass
class SlidesMaster:
    slide_master: Optional[SlideMaster] = field(
        default=None,
        metadata={
            "name": "sldMasterId",
            "type": "Element"
        }
    )


@dataclass
class XmlPresentation(AbstractModel):
    class Meta:
        namespace = NameSpaces.name_space_prs
        name = "presentation"
        path = None
    slides_master: Optional[SlidesMaster] = field(
        default=None,
        metadata={
            "name": "sldMasterIdLst",
            "type": "Element"
        }
    )
    slides: Optional[XmlSlides] = field(
        default=None,
        metadata={
            "name": "sldIdLst",
            "type": "Element"
        }
    )
    slide_size: XmlSlideSize = field(
        default_factory=XmlSlideSize,
        metadata=dict(
            name="sldSz",
            type="Element"
        )
    )
    notes_size: XmlNotesSize = field(
        default_factory=XmlNotesSize,
        metadata=dict(
            name="notesSz",
            type="Element"
        )
    )
    default_text_style: DefaultTextStyle = field(
        default_factory=DefaultTextStyle,
        metadata=dict(
            name="defaultTextStyle",
            type="Element",
            required=True
        )
    )
