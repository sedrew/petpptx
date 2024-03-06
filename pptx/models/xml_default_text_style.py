from dataclasses import field, dataclass
from functools import partial
from typing import Optional

from pptx.models.abstract_dataclass import AbstractModel


@dataclass
class SchemeClr(AbstractModel):
    class Meta:
        name = "schemeClr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    val: Optional[str] = field(
        default="tx1",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SolidFill(AbstractModel):
    class Meta:
        name = "solidFill"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    scheme_clr: Optional[SchemeClr] = field(
        default_factory=SchemeClr,
        metadata={
            "name": "schemeClr",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Latin(AbstractModel):
    class Meta:
        name = "latin"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[str] = field(
        default="+mn-lt",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EastAsian(AbstractModel):
    class Meta:
        name = "ea"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[str] = field(
        default="+mn-ea",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ComplexScript(AbstractModel):
    class Meta:
        name = "cs"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    typeface: Optional[str] = field(
        default="+mn-cs",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DefRpr(AbstractModel):
    """Default Text Run Properties"""
    class Meta:
        name = "defRPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    size: Optional[int] = field(
        default=1800,
        metadata={
            "name": "sz",
            "type": "Attribute",
        }
    )
    kern: Optional[int] = field(
        default=1200,
        metadata={
            "type": "Attribute",
        }
    )
    solid_fill: Optional[SolidFill] = field(
        default_factory=SolidFill,
        metadata={
            "name": "solidFill",
            "type": "Element",
        }
    )
    latin: Optional[Latin] = field(
        default_factory=Latin,
        metadata={
            "type": "Element",
        }
    )
    ea: Optional[EastAsian] = field(
        default_factory=EastAsian,
        metadata={
            "type": "Element",
        }
    )
    cs: Optional[ComplexScript] = field(
        default_factory=ComplexScript,
        metadata={
            "type": "Element",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BaseLevelPr(AbstractModel):
    class Meta:
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    mar_l: Optional[int] = field(
        default=None,
        metadata={
            "name": "marL",
            "type": "Attribute",
            "required": True,
        }
    )
    algn: Optional[str] = field(
        default="l",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    def_tab_sz: Optional[int] = field(
        default=914400,
        metadata={
            "name": "defTabSz",
            "type": "Attribute",
            "required": True,
        }
    )
    rtl: Optional[int] = field(
        default=0,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    ea_ln_brk: Optional[int] = field(
        default=1,
        metadata={
            "name": "eaLnBrk",
            "type": "Attribute",
            "required": True,
        }
    )
    latin_ln_brk: Optional[int] = field(
        default=0,
        metadata={
            "name": "latinLnBrk",
            "type": "Attribute",
            "required": True,
        }
    )
    hanging_punct: Optional[int] = field(
        default=1,
        metadata={
            "name": "hangingPunct",
            "type": "Attribute",
            "required": True,
        }
    )
    def_rpr: Optional[DefRpr] = field(
        default_factory=DefRpr,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class DefPpr(AbstractModel):
    class Meta:
        name = "defPPr"
        namespace = "http://schemas.openxmlformats.org/drawingml/2006/main"

    def_rpr: Optional[DefRpr] = field(
        default=None,
        metadata={
            "name": "defRPr",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class DefaultTextStyle(AbstractModel):
    class Meta:
        name = "defaultTextStyle"
        namespace = "http://schemas.openxmlformats.org/presentationml/2006/main"

    def_ppr: Optional[DefPpr] = field(
        default_factory=lambda: DefPpr(def_rpr=DefRpr(lang="en-US", size=None, solid_fill=None,
                                                      latin=None, ea=None, cs=None)),
        metadata={
            "name": "defPPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl1p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=0),
        metadata={
            "name": "lvl1pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl2p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=457200),
        metadata={
            "name": "lvl2pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl3p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=914400),
        metadata={
            "name": "lvl3pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl4p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=1371600),
        metadata={
            "name": "lvl4pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl5p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=1828800),
        metadata={
            "name": "lvl5pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl6p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=2286000),
        metadata={
            "name": "lvl6pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl7p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=2743200),
        metadata={
            "name": "lvl7pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl8p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=3200400),
        metadata={
            "name": "lvl8pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
    lvl9p_pr: Optional[BaseLevelPr] = field(
        default_factory=partial(BaseLevelPr, mar_l=3657600),
        metadata={
            "name": "lvl9pPr",
            "type": "Element",
            "namespace": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "required": True,
        }
    )
