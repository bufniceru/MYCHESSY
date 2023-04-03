from pieces.Piece import Piece
from pieces.PieceName import PieceName


class Pawn(Piece):
    def __init__(self, square, color):
        super().__init__(square, color)
        self.name = PieceName.pawn



