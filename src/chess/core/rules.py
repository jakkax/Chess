class Rules:
    class Pawn:
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
        
        def attacksSquares(self, board):
            moveDirection = -1 if self.isWhite else 1
            captureSquares = [(self.row + moveDirection, self.column - 1), (self.row + moveDirection, self.column + 1)]
            return captureSquares

    class Rook:
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
        
        def attacksSquares(self, square):
            return self.baseMovement(square)

    class Knight:
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
        
        def attacksSquares(self, square):
            return self.baseMovement(square)

    class Bishop:
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
        
        def attacksSquares(self, square):
            return self.baseMovement(square)

    class Queen:
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
        
        def attacksSquares(self, square):
            return self.baseMovement(square)

    class King:
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
        
        def attacksSquares(self, square):
            return self.baseMovement(square)



# TODO

# rules: contain the blueprints of moves; how to make a move
# engine: applies rules to an actual situation

# rules will have en passant square, castling rights, promotion squares

# GameState (board)
#       ↓
# Engine scans board
#       ↓
# Engine reads piece type
#       ↓
# Rules provide movement pattern
#       ↓
# Engine builds pseudo-legal moves
#       ↓
# Engine simulates moves
#       ↓
# Engine filters illegal moves
