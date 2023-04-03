import sys
import pygame
from pydispatch import dispatcher

from Constants import (
    BOARD_SIDE,
    CELL_SIDE,
    DARK_GREEN,
    LIGHT_GREEN,
    BOARD_START_MOVE,
    BOARD_STOP_MOVE, DRAW_BOARD)
from MouseClick import MouseClick


class Screen:
    def __init__(self):
        """
        Screen initialization
        """
        pygame.init()
        self.screen = pygame.display.set_mode((BOARD_SIDE, BOARD_SIDE))
        pygame.display.set_caption("Chessy")

        #
        # TRACK MOUSE COORDINATES
        #
        self.mouse_click = MouseClick()

        #
        # DRAGGED PIECE AND DRAGGING STATE
        #
        self.dragged_piece = None
        self.dragging = False

    def update(self):
        """
        Screen update
        """
        pygame.display.update()

    def square(self, **kwargs):
        square = kwargs["message"]
        self.draw_square_background(square)
        self.draw_square_piece(square)

    def draw_square_background(self, square):
        color = DARK_GREEN if (square.row + square.column) % 2 else LIGHT_GREEN
        cell_background = (square.column * CELL_SIDE, square.row * CELL_SIDE, CELL_SIDE, CELL_SIDE)
        pygame.draw.rect(self.screen, color, cell_background)

    def draw_square_piece(self, square):
        if square.piece is not None:
            if square.piece.dragged is not True:
                square.piece.set_image(size=80)
                try:
                    img = pygame.image.load(square.piece.image)
                except:
                    print('Cannot load image!')
                else:
                    img_center = square.column * CELL_SIDE + CELL_SIDE // 2, square.row * CELL_SIDE + CELL_SIDE // 2
                    square.piece.image_rect = img.get_rect(center=img_center)
                    self.screen.blit(img, square.piece.image_rect)

    def set_dragged_piece(self, **kwargs):
        """
        Dragged Piese and Dragging State are setted
        """
        self.dragged_piece = kwargs["message"]
        self.dragging = True

    def update_blit(self):
        """
        Uodate Blit with the new dragged position of the dragged Piece
        """
        # image from Piece
        self.dragged_piece.set_image(size=128)
        image = self.dragged_piece.image
        # image for drawing
        img = pygame.image.load(image)
        # rectangle prepare for blitting
        img_center = self.mouse_click()
        self.dragged_piece.image_rect = img.get_rect(center=img_center)
        # blit drowing
        self.screen.blit(img, self.dragged_piece.image_rect)

    def unset_dragged_piece(self, **kwargs):
        """
        Dragged Piese and Dragging State are unsetted
        """
        self.dragged_piece = None
        self.dragging = False

    def loop(self):
        """
        Main Loop of the Screen for Events Processing
        Starting Point of the Program
        """
        while True:
            dispatcher.send(signal=DRAW_BOARD, sender=self, message=None)

            if self.dragging:
                self.update_blit()

            for event in pygame.event.get():
                #
                # MOUSE CLICK
                #
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click.update(event.pos)
                    dispatcher.send(signal=BOARD_START_MOVE, sender=self, message=self.mouse_click.coordinates)
                    dispatcher.send(signal=DRAW_BOARD, sender=self, message=None)

                #
                # MOUSE MOTION
                #
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        self.mouse_click.update(event.pos)
                        dispatcher.send(signal=DRAW_BOARD, sender=self, message=None)
                        self.update_blit()

                #
                # MOUSE RELEASE
                #
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.dragging:
                        self.mouse_click.update(event.pos)

                        dispatcher.send(signal=DRAW_BOARD, sender=self, message=None)
                        dispatcher.send(signal=BOARD_STOP_MOVE, sender=self, message=self.mouse_click.coordinates)

                #
                # QUIT GAME
                #
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                else:
                    ...

            self.update()
