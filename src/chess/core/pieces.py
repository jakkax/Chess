class Piece:
    def __init__(self, colour: bool):
        self.colour = colour # white = True
    
    def generateMoves(self, location, board):
        raise NotImplementedError('Not implemented')

class Pawn(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

class Rook(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

class Knight(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

class Bishop(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

class Queen(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)

class King(Piece):
    def __init__(self, colour: bool):
        super().__init__(colour)
