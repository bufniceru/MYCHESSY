from pieces.Piece import Piece
from pieces.PieceName import PieceName


class Knight(Piece):

    possible_moves = [
        (-2, +1),
        (-1, +2),
        (+1, +2),
        (+2, +1),
        (+2, -1),
        (+1, -2),
        (-1, -2),
        (-2, -1),
    ]

    def __init__(self, square, color):
        super().__init__(square, color)
        self.name = PieceName.knight
