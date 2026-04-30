from .board import Board

class GameState:
    def __init__(self):
        self.board = Board()
        self.board.setupBoard()

        self.isWhiteTurn = True

    def applyMove(self, move):
        self.board.movePiece(move)
        
        self.isWhiteTurn = not self.isWhiteTurn
