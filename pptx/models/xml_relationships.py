from dataclasses import field, dataclass


@dataclass
class XmlRelationship:
    """
    XmlRelationship contains relations which maps id and XML.
    """
    rel_id: str = field(metadata=dict(type="Attribute", name="Id"))
    target: str = field(metadata=dict(type="Attribute", name="Target"))
    type_rels: str = field(metadata=dict(type="Attribute", name="Type"))
    # target_mode: str = field(metadata=dict(type="Attribute", name=)) TODO


@dataclass
class XmlRelationships:
    """
    XmlRelationships describe references from parts to other
    internal resources in the package or to external resources.
    """
    class Meta:
        name = "Relationships"
    xmls: str = field(metadata=dict(type="Attribute", name="http://schemas.openxmlformats.org/package/2006/relationships"))
    relationships: list[XmlRelationship] = field(metadata=dict(name="Relationship"))

