from typing import Union


class Run:

    @property
    def text(self) -> str:
        return ""

    @text.setter
    def text(self, text: str) -> str:
        ...


class Paragraph:

    @property
    def runs(self) -> list[Run]:
        return list()


class TextFrame:

    @property
    def paragraphs(self) -> list[Paragraph]:
        return list()


class Shape:

    @property
    def text_frame(self):
        return


class Slide:

    @property
    def shapes(self) -> list[Union[Shape]]:
        return list()

    @shapes.setter
    def shapes(self, shape) -> list:
        ...


class Presentation:

    @property
    def slides(self) -> list:
        return list()

    @slides.setter
    def slides(self, slide):
        ...
