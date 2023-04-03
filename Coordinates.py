from functools import singledispatchmethod
from types import NoneType


class Coordinates:
    @singledispatchmethod
    def __init__(self, *arg):
        """
        CONSTRUCTOR FROM TUPLE
        """
        self._row, self._column = arg

    @__init__.register(type(None))
    def _from_none(self, value: NoneType):
        """
        CONSTRUCTOR FROM NONE
        """
        self._row = None
        self._column = None

    @__init__.register(str)
    def _from_str(self, notation: str) -> None:
        """
        CONSTRUCTOR FROM STRING
        """
        column, row = notation
        self._column = ord(column) - 97
        self._row = 8 - int(row)


    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    @property
    def rank(self):
        return str(8 - self.row) if self.row is not None else None

    @property
    def file(self):
        return chr(self.column + 97) if self.column is not None else None

    @property
    def notation(self):
        return self.file + self.rank if self.file is not None and self.rank is not None else None

    def __str__(self):
        return f'C({self.row},{self.column})<{self.notation}>'

    def __repr__(self):
        return f'C({self.row},{self.column})<{self.notation}>'