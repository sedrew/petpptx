from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers.config import SerializerConfig

parser_config = ParserConfig(base_url=None, load_dtd=False, process_xinclude=False, fail_on_unknown_properties=False,
                             fail_on_unknown_attributes=False, fail_on_converter_warnings=False)
serialize_config = SerializerConfig(pretty_print=False, xml_declaration=True, ignore_default_attributes=False)