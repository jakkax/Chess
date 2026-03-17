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
        self.board = [[Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False), Knight(False), Rook(False)],
                      [Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False), Pawn(False)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True), Pawn(True)],
                      [Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True), Rook(True)]]
    
    def movePiece(self, move: Move):
        self.board[move.toSquare[0]][move.toSquare[1]] = self.board[move.fromSquare[0]][move.fromSquare[1]]
        self.board[move.fromSquare[0]][move.fromSquare[1]] = None
    
    def unMove(self, move: Move, capturedPiece):
        self.board[move.fromSquare[0]][move.fromSquare[1]] = self.board[move.toSquare[0]][move.toSquare[1]]
        self.board[move.toSquare[0]][move.toSquare[1]] = capturedPiece

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
            board[-1] = '\n'

        return board
