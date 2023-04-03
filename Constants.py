from Color import Color
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook


# DISPATCHER
BOARD_START_MOVE = 'board.start.move'
DRAGGER_START_MOVE = 'dragger.start.move'
SCREEN_SET_DRAGGED_PIECE = 'screen.set.dragged.piece'
BOARD_STOP_MOVE = 'board.stop.move'
DRAGGER_STOP_MOVE = 'dragger.stop.move'
SCREEN_UNSET_DRAGGED_PIECE = 'screen.unset.dragged.piece'
SQUARE_PIECE = 'square.piece'
DRAW_SQUARE = 'draw.square'
DRAW_BOARD = 'draw.board'



# GAME WINDOW DIMENSIONS
BOARD_SIDE = 800

# BOARD
DIMENSION = 8
ROWS = DIMENSION
COLS = DIMENSION
CELL_SIDE = BOARD_SIDE // DIMENSION

DARK_GREEN = (119, 154, 88)
LIGHT_GREEN = (234, 235, 200)

BOARD_INIT = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None]
]

BOARD_START_POSITION = [
    ('a1', Rook(None, Color.white)),
    ('b1', Knight(None, Color.white)),
    ('c1', Bishop(None, Color.white)),
    ('d1', Queen(None, Color.white)),
    ('e1', King(None, Color.white)),
    ('f1', Bishop(None, Color.white)),
    ('g1', Knight(None, Color.white)),
    ('h1', Rook(None, Color.white)),
    ('a2', Pawn(None, Color.white)),
    ('b2', Pawn(None, Color.white)),
    ('c2', Pawn(None, Color.white)),
    ('d2', Pawn(None, Color.white)),
    ('e2', Pawn(None, Color.white)),
    ('f2', Pawn(None, Color.white)),
    ('g2', Pawn(None, Color.white)),
    ('h2', Pawn(None, Color.white)),
    ('a7', Pawn(None, Color.black)),
    ('b7', Pawn(None, Color.black)),
    ('c7', Pawn(None, Color.black)),
    ('d7', Pawn(None, Color.black)),
    ('e7', Pawn(None, Color.black)),
    ('f7', Pawn(None, Color.black)),
    ('g7', Pawn(None, Color.black)),
    ('h7', Pawn(None, Color.black)),
    ('a8', Rook(None, Color.black)),
    ('b8', Knight(None, Color.black)),
    ('c8', Bishop(None, Color.black)),
    ('d8', Queen(None, Color.black)),
    ('e8', King(None, Color.black)),
    ('f8', Bishop(None, Color.black)),
    ('g8', Knight(None, Color.black)),
    ('h8', Rook(None, Color.black))
]
