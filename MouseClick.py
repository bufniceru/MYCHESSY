from Constants import CELL_SIDE


class MouseClick:
    def __init__(self, x=None, y=None):
        self.mouse_x = None
        self.mouse_y = None

    def update(self, mouse_pos):
        """
        Mouse coordinates are updated
        """
        self.mouse_x, self.mouse_y = mouse_pos

    @property
    def coordinates(self):
        return self.mouse_y // CELL_SIDE, self.mouse_x // CELL_SIDE

    def __call__(self):
        return self.mouse_x, self.mouse_y