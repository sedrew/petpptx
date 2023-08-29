from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.openxmlformats.org/presentationml/2006/main"


@dataclass
class CNvPr:
    class Meta:
        name = "cNvPr"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    id: Optional[int] = field(
        default=1,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ClrMapOvr:
    class Meta:
        name = "clrMapOvr"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    master_clr_mapping: Optional[object] = field(
        default=None,
        metadata={
            "name": "masterClrMapping",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
        }
    )


@dataclass
class NvGrpSpPr:
    class Meta:
        name = "nvGrpSpPr"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    c_nv_pr: Optional[CNvPr] = field(
        default_factory=CNvPr,
        metadata={
            "name": "cNvPr",
            "type": "Element",
            "required": True,
        }
    )
    c_nv_grp_sp_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "cNvGrpSpPr",
            "type": "Element",
        }
    )
    nv_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "nvPr",
            "type": "Element",
        }
    )


@dataclass
class SpTree:
    class Meta:
        name = "spTree"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    nv_grp_sp_pr: Optional[NvGrpSpPr] = field(
        default=None,
        metadata={
            "name": "nvGrpSpPr",
            "type": "Element",
            "required": True,
        }
    )
    grp_sp_pr: Optional[object] = field(
        default=None,
        metadata={
            "name": "grpSpPr",
            "type": "Element",
        }
    )


@dataclass
class CSld:
    class Meta:
        name = "cSld"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    sp_tree: Optional[SpTree] = field(
        default_factory=SpTree,
        metadata={
            "name": "spTree",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Slide:
    class Meta:
        name = "sld"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    c_sld: Optional[CSld] = field(
        default_factory=CSld,
        metadata={
            "name": "cSld",
            "type": "Element",
            "required": True,
        }
    )
    clr_map_ovr: Optional[ClrMapOvr] = field(
        default_factory=ClrMapOvr,
        metadata={
            "name": "clrMapOvr",
            "type": "Element",
            "required": True,
        }
    )
