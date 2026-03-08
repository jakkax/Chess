class Engine:
    def isLegalMove(self, move, board):
        piece = board[move.fromSquare[0]][move.fromSquare[1]]
        return move.toSquare in piece.pseudoLegalMoves(board)
