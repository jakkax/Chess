from .board import Position

class GameState:
    def __init__(self):
        self.position = Position()
        self.position.setupBoard()

        self.isWhiteTurn = True
