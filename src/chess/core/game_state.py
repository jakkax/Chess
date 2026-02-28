from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class GameState:
    def __init__(self):
        self.board = None
        self.isWhiteTurn = True
