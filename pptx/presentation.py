# encoding: utf-8

"""Main presentation object."""
from functools import cached_property

from pptx.models.xml_presentation import XmlPresentation
from pptx.package import Package
from pptx.slide import Slide
from pptx.util import lazyproperty


class Presentation:
    """PresentationML (PML) presentation.

    Not intended to be constructed directly. Use :func:`pptx.Presentation` to open or
    create a presentation.
    """
    def __init__(self, pkg, model):
        self._pkg: Package = pkg
        self._model: XmlPresentation = model

    @property
    def model(self) -> XmlPresentation:
        return self._model

    @model.setter
    def model(self, model: XmlPresentation):
        self._model = model

    @property
    def core_properties(self):
        """
        Instance of |CoreProperties| holding the read/write Dublin Core
        document properties for this presentation.
        """
        pass

    @property
    def notes_master(self):
        """
        Instance of |NotesMaster| for this presentation. If the presentation
        does not have a notes master, one is created from a default template
        and returned. The same single instance is returned on each call.
        """
        pass

    def save(self, file):
        """
        Save this presentation to *file*, where *file* can be either a path
        to a file (a string) or a file-like object.
        """
        self._pkg_file.save(file)

    @property
    def slide_height(self) -> int:
        """
        Height of slides in this presentation, in English Metric Units (EMU).
        Returns |None| if no slide width is defined. Read/write.
        """
        return self._model.slide_size.cy

    @slide_height.setter
    def slide_height(self, height: int):
        if 100_000_000 <= height or height < 1_000_000:
            raise ValueError("Value should be more 1_000_000 but less 100_000_000")
        self._model.slide_size.cy = height


    @property
    def slide_layouts(self):
        """
        Sequence of |SlideLayout| instances belonging to the first
        |SlideMaster| of this presentation. A presentation can have more than
        one slide master and each master will have its own set of layouts.
        This property is a convenience for the common case where the
        presentation has only a single slide master.
        """
        pass

    @property
    def slide_master(self):
        """
        First |SlideMaster| object belonging to this presentation. Typically,
        presentations have only a single slide master. This property provides
        simpler access in that common case.
        """
        pass

    @lazyproperty
    def slide_masters(self):
        """
        Sequence of |SlideMaster| objects belonging to this presentation
        """
        pass

    @property
    def slide_width(self) -> int:
        """
        Width of slides in this presentation, in English Metric Units (EMU).
        Returns |None| if no slide width is defined. Read/write.
        """
        return self._model.slide_size.cx

    @slide_width.setter
    def slide_width(self, width: int):
        self._model.slide_size.cx = width

    @cached_property
    def slides(self):
        """
        |Slides| object containing the slides in this presentation.
        """
        return Slide
