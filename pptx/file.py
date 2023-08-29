from dataclasses import dataclass
from collections.abc import Container
from pathlib import Path
from typing import Optional, Any

from pptx.opc.abstract_handler import AbstractHandler
from pptx.opc.package import OpcPackage
from pptx.opc.serialized import PackageReader, _ZipPkgReader, _DirPkgReader, _ZipPkgWriter
from pptx.package import Package


class File:

    def __init__(self, file_path):
        if file_path:
            self.pkg = PackageReader(file_path)._blob_reader._blobs
        else:
            self.pkg = dict()
        self.key_list = list(self.pkg)
        self.queue_models = dict()

    def save(self, file_path):
        out_file = _ZipPkgWriter(file_path)
        self._update_data()
        for el in self.key_list:
            out_file.write(pack_uri=el, blob=self.pkg[el])

    def get_blob(self, key) -> bytes:
        return self.pkg[key]

    def _update_data(self):
        for key, el_handler in self.queue_models.items():
            if key not in self.pkg:
                self.pkg.update({key: el_handler.serializer_model()})
                continue
            self.pkg[key] = el_handler.serializer_model()
