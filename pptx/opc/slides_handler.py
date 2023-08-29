from abc import ABC
from typing import Optional

from pptx.models.xml_presentation import XmlPresentation, NameSpaces, XmlSlide
from pptx.opc.abstract_handler import AbstractHandler
from pptx.opc.base_hanlder import BaseHandler
from pptx.opc.packuri import PackURI


class AbstractSlideHandler(AbstractHandler, ABC):

    def parser_model(self, source: Optional[bytes] = None) -> XmlSlide:
        pass


class SlideHandler(BaseHandler, AbstractSlideHandler):
    def __init__(self, idx: id = 1):
        super(BaseHandler).__init__(name_spaces=NameSpaces.get_namespace_presentation(),
                                    path_pkg=PackURI(f"/ppt/slides/slide{idx}.xml"),
                                    xml_model=XmlSlide)
