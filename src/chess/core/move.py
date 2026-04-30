class Move:
    def __init__(self, fromSquare, toSquare, specialAction = None):
        self.fromSquare = fromSquare
        self.toSquare = toSquare
        self.specialAction = specialAction
    
    def tuplesToMoves(fromSquare, theMoves):
        moves = []

        for move in theMoves:
            moves.append(Move(fromSquare, (move[0], move[1])))

        return moves
