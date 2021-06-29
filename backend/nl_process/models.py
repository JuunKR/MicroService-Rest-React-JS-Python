from dataclasses import dataclass
from common.models import FileDTO, Printer, Reader
import numpy as np
from PIL import Image


@dataclass
class FileDTO(FileDTO):
    img: str

    @property
    def img(self) -> str: return self._img

    @img.setter
    def img(self, img): self._img = img


class Printer(Printer):
    pass


class Reader(Reader):
    # def new_file(self, file) -> str:
    #     if file.img is not None:
    #         return file.context + file.img
    #     else:
    #         return file.context + file.fname
    # def new_img(self, file):
    #     return file.context + file.img

    def txt(self, file) -> str:
        return open(f'{self.new_file(file)}').read()

    def img(self, image):
        return np.array(Image.open(f'{self.new_file(image)}'))

