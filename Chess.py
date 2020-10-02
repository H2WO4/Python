""" Object Definition """

class Board:
    """
    The object Board is used to define a grid in which chess pieces are placed\n
    It contains information about its grid and its grid size
    """
    def __init__(self, size):
        self.grid = []
        self.size = size

        for i in range(size):
            self.grid.append([])
            for j in range(size):
                self.grid[i].append(Blank())

    def __str__(self):
        string = ""
        for i in range(len(self.grid)).__reversed__():
            for j in range(len(self.grid[i])):
                string += str(self.grid[i][j]) + " "
            string += "\n"

        return string

    def initialize(self):
        """ Initialize a 8-size board to classic chess disposition """
        if self.size == 8:
            for i in range(8):
                self.grid[1][i], self.grid[6][i] = Pawn(True), Pawn(False)

            self.grid[0][0], self.grid[7][0] = Rook(True), Rook(False)
            self.grid[0][7], self.grid[7][7] = Rook(True), Rook(False)

            self.grid[0][1], self.grid[7][1] = Fool(True), Fool(False)
            self.grid[0][6], self.grid[7][6] = Fool(True), Fool(False)

            self.grid[0][2], self.grid[7][2] = Knight(True), Knight(False)
            self.grid[0][5], self.grid[7][5] = Knight(True), Knight(False)

            self.grid[0][3], self.grid[7][3] = King(True), King(False)

            self.grid[0][4], self.grid[7][4] = Queen(True), Queen(False)

        else:
            raise TypeError

    def eat(self, eater, eaten):
        """ Handles a piece eating another """
        if eater.white == eaten.white:
            raise TypeError

        self.grid[eater.x][eater.y] = Blank
        self.grid[eaten.x][eaten.y] = eater

        return eaten


class Piece:
    """
    The object Piece is used to define a singular chess piece\n
    It contains information about its color.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = "X"
        self.moved = False

    def __str__(self):
        return self.symbol


class Blank(Piece):
    """
    The object Blank is used to define a singular empty tile\n
    It does not contains any information
    """

    def __init__(self):
        self.symbol = "-"


class Pawn(Piece):
    """
    The object Pawn is used to define a singular chess pawn piece\n
    It contains information about its color, symbol and movement.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = ["♟", "♙"][white]
        self.moved = False


class Rook(Piece):
    """
    The object Rook is used to define a singular chess pawn piece\n
    It contains information about its color, symbol and movement.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = ["♜", "♖"][white]
        self.moved = False


class Fool(Piece):
    """
    The object Fool is used to define a singular chess pawn piece\n
    It contains information about its color, symbol and movement.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = ["♝", "♗"][white]
        self.moved = False


class King(Piece):
    """
    The object King is used to define a singular chess pawn piece\n
    It contains information about its color, symbol and movement.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = ["♚", "♔"][white]
        self.moved = False


class Queen(Piece):
    """
    The object Queen is used to define a singular chess pawn piece\n
    It contains information about its color, symbol and movement.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = ["♛", "♕"][white]
        self.moved = False


class Knight(Piece):
    """
    The object Knight is used to define a singular chess pawn piece\n
    It contains information about its color, symbol and movement.
    """

    def __init__(self, white):
        self.white = white
        self.symbol = ["♞", "♘"][white]
        self.moved = False


MainBoard = Board(8)
MainBoard.initialize()
print(MainBoard)
