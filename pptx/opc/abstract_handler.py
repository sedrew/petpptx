from abc import ABC, abstractmethod
from typing import Optional


class AbstractHandler(ABC):

    @abstractmethod
    def parser_model(self, source: Optional[bytes] = None):
        pass

    @abstractmethod
    def serializer_model(self):
        pass
