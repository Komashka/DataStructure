from Array.arrays import *
from PIL import Image


class GrayscaleImage:
    def __init__(self, nrows, ncols):
        self._rows = nrows
        self._cols = ncols
        self.array = Array2D(nrows, ncols)

    def width(self):
        return self._rows

    def height(self):
        return self._cols

    def clear(self, value):
        for row in range(self.width()):
            row.clear(value)

    def __getitem__(self, row, col):
        return self.array[row, col]

    def __setitem__(self, row, col, value):
        self.array[row, col] = value


photo = Image.open("images.jpeg")
photo = photo.convert("L")
pixel = photo.load()
width, height = photo.size
arr = GrayscaleImage(width, height)
px = photo.load()
px_ = ""
for i in range(5):
    for j in range(5):
        arr.__setitem__(i, j, px[i, j])
        px_ += str((arr.__getitem__(i, j))) + ","
