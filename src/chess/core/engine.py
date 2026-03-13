from copy import deepcopy
from .board import Board
from .game_state import GameState

class Engine:
    def __init__(self):
        self.gameState = GameState()

    def isLegalMove(self, move, board):
        # board = deepcopy(board)

        piece = board[move.fromSquare[0]][move.fromSquare[1]]
        
        # check base movement
        if not move.toSquare in piece.baseMovement(board):
            return False
        
        # checks
        # boardAfterMove = Board()
        # boardAfterMove.board = self.gameState.applyMove(move, board)
        # if boardAfterMove.findKing(self.gameState.isWhiteTurn) in boardAfterMove.attackMap(not self.gameState.isWhiteTurn):
        #     return False

        return True
