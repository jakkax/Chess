class GameState:
    def __init__(self):
        self.board = None
        self.isWhiteTurn = True

    def applyMove(self, move, board):
        # move the piece
        # check for special actions
        # update GameState and board

        fromRow, fromColumn = move.fromSquare[0], move.fromSquare[1]
        toRow, toColumn = move.toSquare[0], move.toSquare[1]

        board[toRow][toColumn] = board[fromRow][fromColumn]
        board[fromRow][fromColumn] = None

        self.isWhiteTurn = not self.isWhiteTurn
