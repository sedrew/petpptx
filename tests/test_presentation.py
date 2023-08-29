from dataclasses import dataclass

from pptx.opc.constants import RELATIONSHIP_TYPE
from pptx.opc.packuri import PackURI
from pptx.opc.serialized import PackageReader, _ZipPkgWriter
from pptx import Presentation
from functools import partial


def test_new_presentation():
    prs = Presentation(r"C:\Users\sedrew\Desktop\pet\python-petpptx\tests\test_files\test_slides.pptx")
    # prs.save(r"C:\Users\sedrew\Desktop\pet\python-petpptx\tests\test_files\test_slides11.pptx")
    assert 1 == 1


def gg(p):
    print(p)
    return f"{p} lll"


def test_manipulate_presentation():

    pp = {
        "a": 23,
        "b": partial(gg, 2),
        "c": partial(gg, 99)
        }

    pp['b'] = pp.get('b')()

    for el in pp.values():
        print(el)

    assert 1 == 1
