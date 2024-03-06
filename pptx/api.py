# encoding: utf-8

"""
Directly exposed API classes, Presentation for now. Provides some syntactic
sugar for interacting with the pptx.presentation.Package graph and also
provides some insulation so not so many classes in the other modules need to
be named as internal (leading underscore).
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import os
from io import BytesIO
from pathlib import Path

from pptx.models.constants import CONTENT_TYPE as CT
from .opc.packuri import PackURI
from .package import Package
from .presentation import Presentation


def presentation(pptx: str | Path | BytesIO = None) -> Presentation:
    """
    Return a |Presentation| object loaded from *pptx*, where *pptx* can be
    either a path to a ``.pptx`` file (a string) or a file-like object. If
    *pptx* is missing or ``None``, the built-in default presentation
    "template" is loaded.
    """
    pkg = Package()
    if pptx is None:
        pkg.create_presentation()
    pkg.open_presentation(pptx)

    # if not _is_pptx_package(presentation_part):
    #     tmpl = "file '%s' is not a PowerPoint file, content type is '%s'"
    #     raise ValueError(tmpl % (pptx, presentation_part.content_type))

    return Presentation(pkg=pkg, model=pkg.get_model(PackURI("/ppt/presentation.xml")))


def _default_pptx_path():
    """
    Return the path to the built-in default .pptx package.
    """
    _thisdir = os.path.split(__file__)[0]
    return os.path.join(_thisdir, "templates", "default.pptx")


def _is_pptx_package(prs_part):
    """
    Return |True| if *prs_part* is a valid main document part, |False|
    otherwise.
    """
    valid_content_types = (CT.PML_PRESENTATION_MAIN, CT.PML_PRES_MACRO_MAIN)
    return prs_part.content_type in valid_content_types
