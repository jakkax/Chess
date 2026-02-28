from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board = [[None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8]
        
        self.isWhiteTurn = True
    
    def setupBoard(self, whiteView):
        self.board = [[Rook(not whiteView, 0, 0), Knight(not whiteView, 0, 1), Bishop(not whiteView, 0, 2), Queen(not whiteView, 0, 3), King(not whiteView, 0, 4), Bishop(not whiteView, 0, 5), Knight(not whiteView, 0, 6), Rook(not whiteView, 0, 7)],
                      [Pawn(not whiteView, 1, 0), Pawn(not whiteView, 1, 1), Pawn(not whiteView, 1, 2), Pawn(not whiteView, 1, 3), Pawn(not whiteView, 1, 4), Pawn(not whiteView, 1, 5), Pawn(not whiteView, 1, 6), Pawn(not whiteView, 1, 7)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(whiteView, 6, 0), Pawn(whiteView, 6, 1), Pawn(whiteView, 6, 2), Pawn(whiteView, 6, 3), Pawn(whiteView, 6, 4), Pawn(whiteView, 6, 5), Pawn(whiteView, 6, 6), Pawn(whiteView, 6, 7)],
                      [Rook(whiteView, 7, 0), Knight(whiteView, 7, 1), Bishop(whiteView, 7, 2), Queen(whiteView, 7, 3), King(whiteView, 7, 4), Bishop(whiteView, 7, 5), Knight(whiteView, 7, 6), Rook(whiteView, 7, 7)]]

    def __str__(self):
        board = ''

        for row in self.board:
            for piece in row:
                if piece.__str__() == 'None':
                    board += '______ '
                else:
                    board += piece.__str__() + ' '
            board = board[:-1]
            board += '\n'

        return board
