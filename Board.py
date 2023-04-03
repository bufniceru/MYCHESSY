from pydispatch import dispatcher

from Constants import (
    BOARD_INIT,
    DIMENSION,
    SQUARE_PIECE,
    BOARD_START_POSITION,
    DRAGGER_START_MOVE,
    DRAGGER_STOP_MOVE, DRAW_SQUARE)
from Coordinates import Coordinates
from Square import Square


class Board:
    def __init__(self, my_color):
        self.squares = BOARD_INIT
        self.create()
        self.set_pieces_initial_position()
        self.my_color = my_color
        self.piece_dragged = None

    def create(self):
        """
        Create an empty Board
        """
        for row in range(DIMENSION):
            for column in range(DIMENSION):
                self.squares[row][column] = Square(self, row, column)

    def set_pieces_initial_position(self):
        """
        Fill the empty Board with initial position of all Pieces
        A list with all Pieces is iterated
        """
        for piece in BOARD_START_POSITION:
            self.add_piece(*piece)

    def add_piece(self, notation, piece):
        """
        A piece is added to the Board
        """
        coordinates = Coordinates(notation)
        piece.square = self.squares[coordinates.row][coordinates.column]
        self.squares[coordinates.row][coordinates.column].add_piece(piece)

    # def process_pieces(self):
    #     """
    #     All Pieces are iterated for Drawing on the Screen
    #     """
    #     for row in range(DIMENSION):
    #         for col in range(DIMENSION):
    #             if self.squares[row][col].piece is not None:
    #                 dispatcher.send(signal=SQUARE_PIECE, sender=self, message=self.squares[row][col])

    def draw(self):
        """
        All Squares are iterated for Drawing on the Screen
        """
        for square in self.get_suares():
            dispatcher.send(signal=DRAW_SQUARE, sender=self, message=square)

    def get_suares(self):
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                yield self.squares[row][col]

    def start_move(self, **kwargs):
        """
        Start a Move in the Board
        """
        clicked_row, clicked_column = kwargs["message"]
        clicked_piece = self.squares[clicked_row][clicked_column].piece
        if clicked_piece is not None:
            clicked_piece.dragged = True
            self.piece_dragged = clicked_piece
            print(f'BOARD START MOVE {clicked_piece.notation} {clicked_piece.name.name} {clicked_piece.color.name}')
            dispatcher.send(signal=DRAGGER_START_MOVE, sender=self, message=self.squares[clicked_row][clicked_column])

    def stop_move(self, **kwargs):
        """
        Stop a Move in the Board
        """
        release_row, released_column = kwargs["message"]
        self.piece_dragged.dragged = False
        self.piece_dragged = None
        print(f'BOARD STOP MOVE {self.squares[release_row][released_column].notation}')
        dispatcher.send(signal=DRAGGER_STOP_MOVE, sender=self, message=self.squares[release_row][released_column])

    #
    # CALL
    #
    def __call__(self, notation):
        coordinates = Coordinates(notation)
        return self.squares[coordinates.row][coordinates.column]