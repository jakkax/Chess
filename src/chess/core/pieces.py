class Piece:
    def __init__(self, isWhite, row, column):
        self.isWhite = isWhite
        self.row = row
        self.column = column
    
    def pseudoLegalMoves(self, board):
        pass
    
    def __str__(self):
        return 'piece'

class Pawn(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def pseudoLegalMoves(self, board): # all possible ways a piece can move regardless of rules
        pass
    
    def __str__(self):
        return ' pawn '

class Rook(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def pseudoLegalMoves(self, board):
        pseudoLegalMoves = []
        
        moveDirections = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for r, c in moveDirections:
            row, column = self.row, self.column
            while True:
                row += r
                column += c
                if row not in range(8) or column not in range(8):
                    break
                
                if board[row][column] is None:
                    pseudoLegalMoves.append((row, column))
                    continue
                
                if board[row][column].isWhite != self.isWhite:
                    pseudoLegalMoves.append((row, column))
                    break
        
        return pseudoLegalMoves
    
    def __str__(self):
        return ' rook '

class Knight(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def pseudoLegalMoves(self, board):
        r, c = self.row, self.column
        possibleMoves = [(r - 1, c - 2), (r + 1, c - 2), (r - 2, c - 1), (r - 2, c + 1), (r + 2, c - 1), (r + 2, c + 1), (r - 1, c + 2), (r + 1, c + 2)]
        pseudoLegalMoves = []
        
        for square in possibleMoves:
            row = square[0]
            column = square[1]
            if row not in range(8) or column not in range(8):
                continue

            if board[row][column] is None or board[row][column].isWhite != self.isWhite:
                pseudoLegalMoves.append(square)
        
        return pseudoLegalMoves
    
    def __str__(self):
        return 'knight'

class Bishop(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def pseudoLegalMoves(self, board):
        pseudoLegalMoves = []
        
        moveDirections = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        for r, c in moveDirections:
            row, column = self.row, self.column
            while True:
                row += r
                column += c
                if row not in range(8) or column not in range(8):
                    break
                
                if board[row][column] is None:
                    pseudoLegalMoves.append((row, column))
                    continue
                
                if board[row][column].isWhite != self.isWhite:
                    pseudoLegalMoves.append((row, column))
                    break
        
        return pseudoLegalMoves
    
    def __str__(self):
        return 'bishop'

class Queen(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def pseudoLegalMoves(self, board):
        pseudoLegalMoves = []
        
        moveDirections = [(-1, -1), (1, -1), (1, 1), (-1, 1), (-1, 0), (0, -1), (1, 0), (0, 1)]
        for r, c in moveDirections:
            row, column = self.row, self.column
            while True:
                row += r
                column += c
                if row not in range(8) or column not in range(8):
                    break
                
                if board[row][column] is None:
                    pseudoLegalMoves.append((row, column))
                    continue
                
                if board[row][column].isWhite != self.isWhite:
                    pseudoLegalMoves.append((row, column))
                    break
        
        return pseudoLegalMoves
    
    def __str__(self):
        return 'queen '

class King(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def pseudoLegalMoves(self, board):
        pseudoLegalMoves = []
        
        for r in range(-1, 2): # -1, 0, 1
            for c in range(-1, 2):
                row = self.row + r
                column = self.column + c
                
                if row not in range(8) or column not in range(8) or (r == 0 and c == 0):
                    continue
                
                if board[row][column] is None or board[row][column].isWhite != self.isWhite:
                    pseudoLegalMoves.append((row, column))
        
        return pseudoLegalMoves
    
    def __str__(self):
        return ' king '
