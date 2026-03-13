class GameState:
    def __init__(self):
        self.isWhiteTurn = True

    def applyMove(self, move, board):
        # move the piece
        # check for special actions

        fromRow, fromColumn = move.fromSquare[0], move.fromSquare[1]
        toRow, toColumn = move.toSquare[0], move.toSquare[1]

        board[toRow][toColumn] = board[fromRow][fromColumn]
        board[fromRow][fromColumn] = None

        return board
