from Coordinates import Coordinates


class Square:
    def __init__(self, board, row, column, piece=None):
        self.board = board
        self.coordinates = Coordinates(row, column)
        self.piece = piece

    @property
    def row(self):
        return self.coordinates.row

    @property
    def column(self):
        return self.coordinates.column

    @property
    def notation(self):
        return self.coordinates.notation

    @property
    def has_piece(self):
        return self.piece is not None

    @property
    def is_empty(self):
        return not self.has_piece

    @property
    def has_my_piece(self):
        return self.has_piece and self.piece.color == self.board.my_color

    @property
    def has_rival_piece(self):
        return self.has_piece and self.piece.color != self.board.my_color

    @property
    def isempty_or_rival(self):
        return self.is_empty or self.has_rival_piece

    def add_piece(self, piece):
        self.piece = piece

    def __str__(self):
        return f'{self.coordinates}'

