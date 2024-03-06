from dataclasses import dataclass
from pptx.models.abstract_dataclass import AbstractModel


@dataclass
class NameSpaces(AbstractModel):
    _name_space = {
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        "p": "http://schemas.openxmlformats.org/presentationml/2006/main"
    }

    source_relationship = _name_space.get('r')
    name_space_prs = _name_space.get('p')
    drawing_ml = _name_space.get('a')

    @classmethod
    def get_namespace_map(cls) -> dict:
        return cls._name_space

    @classmethod
    def get_namespace_presentation(cls):
        return dict((tag, url) for tag, url in zip(('a', 'r', 'p'), cls._name_space))
