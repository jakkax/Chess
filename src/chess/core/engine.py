from .board import Position
from .game_state import GameState
from .move import Move

class Engine:
    def isLegalMove(self, move: Move, gameState: GameState):
        piece = gameState.position.board[move.fromSquare[0]][move.fromSquare[1]]
        capturedPiece = gameState.position.board[move.toSquare[0]][move.toSquare[1]]
        
        # check base movement
        if not move.toSquare in piece.baseMovement(gameState.position.board):
            return False
        
        # checks
        gameState.position.movePiece(move)
        if gameState.position.findKing(gameState.isWhiteTurn) in gameState.position.board.attackMap(not gameState.isWhiteTurn):
            gameState.position.unMove(move, capturedPiece)
            return False
        gameState.position.unMove(move, capturedPiece)

        return True
