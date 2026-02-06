from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class GameState:
    def __init__(self):
        self.board = [[None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8]
    
    def setupBoard(self, whiteView):
        self.board = [[Rook(not whiteView), Knight(not whiteView), Bishop(not whiteView), Queen(not whiteView), King(not whiteView), Bishop(not whiteView), Knight(not whiteView), Rook(not whiteView)],
                      [Pawn(not whiteView), Pawn(not whiteView), Pawn(not whiteView), Pawn(not whiteView), Pawn(not whiteView), Pawn(not whiteView), Pawn(not whiteView), Pawn(not whiteView)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(whiteView), Pawn(whiteView), Pawn(whiteView), Pawn(whiteView), Pawn(whiteView), Pawn(whiteView), Pawn(whiteView), Pawn(whiteView)],
                      [Rook(whiteView), Knight(whiteView), Bishop(whiteView), Queen(whiteView), King(whiteView), Bishop(whiteView), Knight(whiteView), Rook(whiteView)]]
