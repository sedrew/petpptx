from typing import Optional

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from pptx.models.abstract_dataclass import AbstractModel
from pptx.opc import parser_config, serialize_config
from pptx.opc.abstract_handler import AbstractHandler
from pptx.opc.packuri import PackURI


class BaseHandler(AbstractHandler):

    xml_parser: XmlParser = XmlParser(config=parser_config)
    xml_serializer: XmlSerializer = XmlSerializer(config=serialize_config)
    abstract_type: AbstractModel

    def __init__(self, xml_model, path_pkg: str, name_spaces: dict):
        self.path_pkg = path_pkg
        self.model = xml_model()
        self.xml_model = xml_model
        self.name_spaces = name_spaces

    def parser_model(self, source: Optional[bytes] = None) -> AbstractModel:
        if source:
            self.model = self.xml_parser.from_bytes(source=source, clazz=self.xml_model)
        return self.model

    def serializer_model(self) -> bytes:
        return self.serializer_model_to_str(self.model).encode('utf-8')

    def serializer_model_to_str(self, model: AbstractModel) -> str:
        return self.xml_serializer.render(model, ns_map=self.name_spaces)

