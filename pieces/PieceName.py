import enum


class PieceName(enum.Enum):
    pawn = 1_000
    knight = 3_000
    bishop = 3_001
    rook = 5_000
    queen = 9_000
    king = 10_000_000
