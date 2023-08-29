import zipfile
from collections.abc import Container

from pptx.opc.packuri import PackURI
from pptx.opc.serialized import PackageReader, PackageWriter, _ZipPkgWriter


class _ZipPkgReader(dict):
    """Implements |PhysPkgReader| interface for a zip-file OPC package."""

    def __init__(self, pkg_file):
        super().__init__()
        self._pkg_file = pkg_file

    def __contains__(self, pack_uri):
        """Return True when part identified by `pack_uri` is present in zip archive."""
        return pack_uri in self._blobs

    def __getitem__(self, pack_uri):
        """Return bytes for part corresponding to `pack_uri`.

        Raises |KeyError| if no matching member is present in zip archive.
        """
        if pack_uri not in self._blobs:
            raise KeyError("no member '%s' in package" % pack_uri)
        return self._blobs[pack_uri]

    @property
    def _blobs(self):
        """dict mapping partname to package part binaries."""
        with zipfile.ZipFile(self._pkg_file, "r") as z:
            return {PackURI("/%s" % name): z.read(name) for name in z.namelist()}


def test_ser():
    pp = _ZipPkgReader(r"C:\Users\sedrew\Desktop\pet\python-petpptx\tests\test_files\test_slides.pptx")
    #print(list(pp._blobs))
   # pp.pop(PackURI('/ppt/presentation.xml'))
    pp.get(PackURI('/ppt/presentation.xml'))
    print(pp[PackURI('/ppt/presentation.xml')])

    assert 1 == 1


def test_package_reader():
    file = PackageReader(r"C:\Users\sedrew\Desktop\pet\python-petpptx\tests\test_files\test_slides.pptx")
    vb = file._blob_reader
    pp = _ZipPkgWriter(r"C:\Users\sedrew\Desktop\pet\python-petpptx\tests\test_files\test_slides333.pptx")

    print(list(vb._blobs))
    pp.write(pack_uri=list(vb._blobs)[1], blob=vb._blobs[list(vb._blobs)[1]])

    #print(vb)
    assert 1 == 1
