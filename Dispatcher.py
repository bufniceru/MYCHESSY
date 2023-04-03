from pydispatch import dispatcher

from Board import Board
from Constants import (
    BOARD_START_MOVE,
    DRAGGER_START_MOVE,
    SCREEN_SET_DRAGGED_PIECE,
    BOARD_STOP_MOVE,
    DRAGGER_STOP_MOVE,
    SCREEN_UNSET_DRAGGED_PIECE, DRAW_SQUARE, DRAW_BOARD)
from Dragger import Dragger
from Screen import Screen


class Dispatcher:
    def __init__(self, my_color):
        self.board = Board(my_color)
        self.screen = Screen()
        self.dragger = Dragger()

        #
        # DRAW BOARD
        #
        dispatcher.connect(
            self.board.draw,
            signal=DRAW_BOARD,
            sender=dispatcher.Any
        )

        #
        # DRAW A SQUARE WITH OR WITHOUT A PIECE
        #
        dispatcher.connect(
            self.screen.square,
            signal=DRAW_SQUARE,
            sender=dispatcher.Any
        )

        #
        # START A MOVE IN BOARD
        #
        dispatcher.connect(
            self.board.start_move,
            signal=BOARD_START_MOVE,
            sender=dispatcher.Any
        )

        #
        # START A MOVE IN DRAGGER
        #
        dispatcher.connect(
            self.dragger.start_move,
            signal=DRAGGER_START_MOVE,
            sender=dispatcher.Any
        )

        #
        # SET DRAGGED PIECE IN SCREEN
        #
        dispatcher.connect(
            self.screen.set_dragged_piece,
            signal=SCREEN_SET_DRAGGED_PIECE,
            sender=dispatcher.Any
        )

        #
        # STOP A MOVE IN BOARD
        #
        dispatcher.connect(
            self.board.stop_move,
            signal=BOARD_STOP_MOVE,
            sender=dispatcher.Any
        )

        #
        # STOP A MOVE IN DRAGGER
        #
        dispatcher.connect(
            self.dragger.stop_move,
            signal=DRAGGER_STOP_MOVE,
            sender=dispatcher.Any
        )

        #
        # UNSET DRAGGED PIECE IN SCREEN
        #
        dispatcher.connect(
            self.screen.unset_dragged_piece,
            signal=SCREEN_UNSET_DRAGGED_PIECE,
            sender=dispatcher.Any
        )


