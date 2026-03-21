from .move import Move

class Engine:
    def __init__(self, gameState):
        self.gameState = gameState
    
    def isLegalMove(self, move: Move):
        piece = self.gameState.position.board[move.fromSquare[0]][move.fromSquare[1]]
        capturedPiece = self.gameState.position.board[move.toSquare[0]][move.toSquare[1]]
        
        # check base movement
        if not move.toSquare in piece.baseMovement(self.gameState.position.board):
            return False
        
        # checks
        self.gameState.position.movePiece(move)
        if self.gameState.position.findKing(self.gameState.isWhiteTurn) in self.gameState.position.attackMap(not self.gameState.isWhiteTurn):
            self.gameState.position.unMove(move, capturedPiece)
            return False
        else:
            self.gameState.position.unMove(move, capturedPiece)
            return True
