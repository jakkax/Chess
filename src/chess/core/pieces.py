class Piece:
    def __init__(self, isWhite, row, column):
        self.isWhite = isWhite
        self.row = row
        self.column = column
    
    def baseMovement(self, board): # all possible ways a piece can move regardless of rules
        pass

    def attacksSquares(self, board):
        return self.baseMovement(board)
    
    def __str__(self):
        return 'piece'

class Pawn(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def attacksSquares(self, board):
        moveDirection = -1 if self.isWhite else 1
        captureSquares = [(self.row + moveDirection, self.column - 1), (self.row + moveDirection, self.column + 1)]
        return captureSquares
    
    def baseMovement(self, board):
        moveDirection = -1 if self.isWhite else 1
        doubleMoveRow = 6 if self.isWhite else 1
        baseMovement = []

        if board[self.row + moveDirection][self.column] is None:
            baseMovement.append((self.row + moveDirection, self.column))
            if self.row == doubleMoveRow and board[self.row + 2*moveDirection][self.column] is None:
                baseMovement.append((self.row + 2*moveDirection, self.column))
        
        for capture in [(self.row + moveDirection, self.column - 1), (self.row + moveDirection, self.column + 1)]:
            if capture[1] not in range(8) or capture[0] not in range(8):
                continue

            piece = board[capture[0]][capture[1]]
            if piece is not None and piece.isWhite != self.isWhite:
                baseMovement.append(capture)
        
        return baseMovement
    
    def __str__(self):
        return ' pawn '

class Rook(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def baseMovement(self, board):
        baseMovement = []
        
        moveDirections = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for r, c in moveDirections:
            row, column = self.row, self.column
            while True:
                row += r
                column += c
                if row not in range(8) or column not in range(8):
                    break
                
                if board[row][column] is None:
                    baseMovement.append((row, column))
                    continue
                
                if board[row][column].isWhite != self.isWhite:
                    baseMovement.append((row, column))
                
                break
        
        return baseMovement
    
    def __str__(self):
        return ' rook '

class Knight(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def baseMovement(self, board):
        r, c = self.row, self.column
        possibleMoves = [(r - 1, c - 2), (r + 1, c - 2), (r - 2, c - 1), (r - 2, c + 1), (r + 2, c - 1), (r + 2, c + 1), (r - 1, c + 2), (r + 1, c + 2)]
        baseMovement = []
        
        for square in possibleMoves:
            row = square[0]
            column = square[1]
            if row not in range(8) or column not in range(8):
                continue

            if board[row][column] is None or board[row][column].isWhite != self.isWhite:
                baseMovement.append(square)
        
        return baseMovement
    
    def __str__(self):
        return 'knight'

class Bishop(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def baseMovement(self, board):
        baseMovement = []
        
        moveDirections = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        for r, c in moveDirections:
            row, column = self.row, self.column
            while True:
                row += r
                column += c
                if row not in range(8) or column not in range(8):
                    break
                
                if board[row][column] is None:
                    baseMovement.append((row, column))
                    continue
                
                if board[row][column].isWhite != self.isWhite:
                    baseMovement.append((row, column))
                
                break
        
        return baseMovement
    
    def __str__(self):
        return 'bishop'

class Queen(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def baseMovement(self, board):
        baseMovement = []
        
        moveDirections = [(-1, -1), (1, -1), (1, 1), (-1, 1), (-1, 0), (0, -1), (1, 0), (0, 1)]
        for r, c in moveDirections:
            row, column = self.row, self.column
            while True:
                row += r
                column += c
                if row not in range(8) or column not in range(8):
                    break
                
                if board[row][column] is None:
                    baseMovement.append((row, column))
                    continue
                
                if board[row][column].isWhite != self.isWhite:
                    baseMovement.append((row, column))
                
                break
        
        return baseMovement
    
    def __str__(self):
        return 'queen '

class King(Piece):
    def __init__(self, isWhite, row, column):
        super().__init__(isWhite, row, column)
    
    def baseMovement(self, board):
        baseMovement = []
        
        for r in range(-1, 2): # -1, 0, 1
            for c in range(-1, 2):
                row = self.row + r
                column = self.column + c
                
                if row not in range(8) or column not in range(8) or (r == 0 and c == 0):
                    continue
                
                if board[row][column] is None or board[row][column].isWhite != self.isWhite:
                    baseMovement.append((row, column))
        
        return baseMovement
    
    def __str__(self):
        return ' king '
