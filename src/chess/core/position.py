from .pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King
from .move import Move

class Position:
    def __init__(self):
        self.board = [[None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8,
                      [None] * 8]
    
    def setupBoard(self):
        self.board = [[Rook(False, 0, 0), Knight(False, 0, 1), Bishop(False, 0, 2), Queen(False, 0, 3), King(False, 0, 4), Bishop(False, 0, 5), Knight(False, 0, 6), Rook(False, 0, 7)],
                      [Pawn(False, 1, 0), Pawn(False, 1, 1), Pawn(False, 1, 2), Pawn(False, 1, 3), Pawn(False, 1, 4), Pawn(False, 1, 5), Pawn(False, 1, 6), Pawn(False, 1, 7)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(True, 6, 0), Pawn(True, 6, 1), Pawn(True, 6, 2), Pawn(True, 6, 3), Pawn(True, 6, 4), Pawn(True, 6, 5), Pawn(True, 6, 6), Pawn(True, 6, 7)],
                      [Rook(True, 7, 0), Knight(True, 7, 1), Bishop(True, 7, 2), Queen(True, 7, 3), King(True, 7, 4), Bishop(True, 7, 5), Knight(True, 7, 6), Rook(True, 7, 7)]]
    
    def movePiece(self, move: Move):
        self.board[move.toSquare[0]][move.toSquare[1]] = self.board[move.fromSquare[0]][move.fromSquare[1]]
        self.board[move.fromSquare[0]][move.fromSquare[1]] = None
        
        piece: Piece = self.board[move.toSquare[0]][move.toSquare[1]]
        piece.row = move.toSquare[0]
        piece.column = move.toSquare[1]
    
    def unMove(self, move: Move, capturedPiece = None):
        self.board[move.fromSquare[0]][move.fromSquare[1]] = self.board[move.toSquare[0]][move.toSquare[1]]
        self.board[move.toSquare[0]][move.toSquare[1]] = capturedPiece

        piece: Piece = self.board[move.fromSquare[0]][move.fromSquare[1]]
        piece.row = move.fromSquare[0]
        piece.row = move.fromSquare[1]

    def attackMap(self, colour):
        attackMap = set()

        for row in self.board:
            for piece in row:
                if piece is None:
                    continue
                
                if piece.isWhite == colour:
                    attackMap.update(piece.attacksSquares(self.board))
        
        return list(attackMap)
    
    def findKing(self, colour):
        for rowIndex, row in enumerate(self.board):
            for columnIndex, piece in enumerate(row):
                if piece is None:
                    continue

                if type(piece).__name__.lower() == 'king' and piece.isWhite == colour:
                    return (rowIndex, columnIndex)

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
