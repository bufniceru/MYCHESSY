from pydispatch import dispatcher

from Constants import (
    SCREEN_SET_DRAGGED_PIECE,
    SCREEN_UNSET_DRAGGED_PIECE)


class Dragger:
    def __init__(self):
        self.dragged_piece = None
        self.dragging = False
        self.initial_row = 0
        self.initial_col = 0

    def start_move(self, **kwargs):
        """
        Start a Move in Dragger
        """
        clicked_square = kwargs["message"]
        self.save_initial(clicked_square)
        self.drag_piece(clicked_square)
        dispatcher.send(signal=SCREEN_SET_DRAGGED_PIECE, sender=self, message=clicked_square.piece)

    def save_initial(self, clicked_square):
        """
        Save initial positions of dragging piece
        """
        # print(f'DRAGGER START MOVE {clicked_square.piece.notation}')
        self.initial_row = clicked_square.row
        self.initial_col = clicked_square.column

    def drag_piece(self, clicked_square):
        """
        Save the dragged Piece and dragging state
        """
        # print(f'DRAGGER START PIECE {clicked_square.piece.name.name}')
        self.dragged_piece = clicked_square.piece
        self.dragging = True

    def stop_move(self, **kwargs):
        """
        Stop a Move in Dragger
        """
        released_square = kwargs["message"]
        self.undrag_piece()

    def undrag_piece(self):
        """
        Reset the dragged Piece and dragging state
        """
        self.dragged_oiece = None
        self.dragging = False
        dispatcher.send(signal=SCREEN_UNSET_DRAGGED_PIECE, sender=self, message=None)
