class Move:
    def __init__(self, fromSquare, toSquare, specialAction = None):
        self.fromSquare = fromSquare
        self.toSquare = toSquare
        self.specialAction = specialAction
