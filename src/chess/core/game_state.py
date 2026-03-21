from .position import Position

class GameState:
    def __init__(self):
        self.position = Position()
        self.position.setupBoard()

        self.isWhiteTurn = True

    def applyMove(self, move):
        self.position.movePiece(move)
        
        self.isWhiteTurn = not self.isWhiteTurn
