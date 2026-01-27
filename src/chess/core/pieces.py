class Piece:
    def __init__(self, colour: str):
        self.colour = colour
    
    def generateMoves(self, location, board):
        raise NotImplementedError('Not implemented')

class Pawn(Piece):
    def __init__(self, colour: str):
        super().__init__(colour)

class Rook(Piece):
    def __init__(self, colour: str):
        super().__init__(colour)

class Knight(Piece):
    def __init__(self, colour: str):
        super().__init__(colour)

class Bishop(Piece):
    def __init__(self, colour: str):
        super().__init__(colour)

class Queen(Piece):
    def __init__(self, colour: str):
        super().__init__(colour)

class King(Piece):
    def __init__(self, colour: str):
        super().__init__(colour)
