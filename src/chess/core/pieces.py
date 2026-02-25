class Piece:
    def __init__(self, isWhite, row, column):
        self.isWhite = isWhite
        self.row = row
        self.column = column
    
    def generateMoves(self, location, board):
        raise NotImplementedError('Not implemented')
    
    def __str__(self):
        return 'piece'

class Pawn(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def __str__(self):
        return ' pawn '

class Rook(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def __str__(self):
        return ' rook '

class Knight(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def __str__(self):
        return 'knight'

class Bishop(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def __str__(self):
        return 'bishop'

class Queen(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def __str__(self):
        return 'queen '

class King(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def __str__(self):
        return ' king '
