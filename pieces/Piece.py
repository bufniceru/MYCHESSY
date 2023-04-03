import os


class Piece:
    def __init__(self, square, color):
        self.square = square
        self.color = color
        self.name = None
        self.image = None
        self.image_rect = None
        self.dragged = False

    @property
    def row(self):
        return self.square.coordinates.row

    @property
    def column(self):
        return self.square.coordinates.column

    @property
    def notation(self):
        return self.square.coordinates.notation

    def set_image(self, size=80):
        self.image = os.path.join(
            f'assets/images/imgs-{size}px/{self.color.name}_{self.name.name}.png')

    def __str__(self):
        # return f'{self.name.name}-{self.color.name}({self.notation})'
        return f'{self.name.name}-{self.color.name})'


