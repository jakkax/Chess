Rook, Knight, Bishop, Queen, King, Pawn = None

class Board:
    def __init__(self):
        self.board = [[Rook(False, 0, 0), Knight(False, 0, 1), Bishop(False, 0, 2), Queen(False, 0, 3), King(False, 0, 4), Bishop(False, 0, 5), Knight(False, 0, 6), Rook(False, 0, 7)],
                      [Pawn(False, 1, 0), Pawn(False, 1, 1), Pawn(False, 1, 2), Pawn(False, 1, 3), Pawn(False, 1, 4), Pawn(False, 1, 5), Pawn(False, 1, 6), Pawn(False, 1, 7)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(True, 6, 0), Pawn(True, 6, 1), Pawn(True, 6, 2), Pawn(True, 6, 3), Pawn(True, 6, 4), Pawn(True, 6, 5), Pawn(True, 6, 6), Pawn(True, 6, 7)],
                      [Rook(True, 7, 0), Knight(True, 7, 1), Bishop(True, 7, 2), Queen(True, 7, 3), King(True, 7, 4), Bishop(True, 7, 5), Knight(True, 7, 6), Rook(True, 7, 7)]