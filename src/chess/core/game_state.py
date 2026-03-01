from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class GameState:
    def __init__(self):
        self.board = None
        self.isWhiteTurn = True

    def applyMove(self, move, board):
        pass
        # move the piece
        # check for special actions
        # update GameState and board