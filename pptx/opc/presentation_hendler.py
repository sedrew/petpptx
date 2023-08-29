from typing import Optional

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from pptx.models.xml_presentation import XmlPresentation, NameSpaces
from pptx.opc import parser_config, serialize_config
from pptx.opc.abstract_handler import AbstractHandler


class PresentationHandler(AbstractHandler):
    xml_parser: XmlParser = XmlParser(config=parser_config)
    xml_serializer: XmlSerializer = XmlSerializer(config=serialize_config)

    def __init__(self):
        self.path_pkg: str = "/ppt/presentation.xml"
        self.model = XmlPresentation()

    def parser_model(self, source: Optional[bytes] = None) -> XmlPresentation:
        if source:
            self.model = self.xml_parser.from_bytes(source=source, clazz=XmlPresentation)
        return self.model

    def serializer_model(self) -> bytes:
        return self.serializer_model_to_str(self.model).encode('utf-8')

    @classmethod
    def serializer_model_to_str(cls, model: XmlPresentation) -> str:
        return cls.xml_serializer.render(model, ns_map=NameSpaces.get_namespace_presentation())
