from .board import Position
from .game_state import GameState
from .move import Move

class Engine:
    def isLegalMove(self, move: Move, board: Position, gameState):
        piece = board.board[move.fromSquare[0]][move.fromSquare[1]]
        capturedPiece = board.board[move.toSquare[0]][move.toSquare[1]]
        
        # check base movement
        if not move.toSquare in piece.baseMovement(board.board):
            return False
        
        # checks
        board.movePiece(move)
        if board.findKing(gameState.isWhiteTurn) in board.attackMap(not gameState.isWhiteTurn):
            board.unMove(move, capturedPiece)
            return False
        board.unMove(move, capturedPiece)

        return True
