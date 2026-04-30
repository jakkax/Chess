from .move import Move

class Engine:
    def __init__(self, gameState):
        self.gameState = gameState
    
    def isLegalMove(self, move: Move):
        piece = self.gameState.board.coords(move.fromSquare)
        capturedPiece = self.gameState.board.coords(move.toSquare)
        
        # check base movement
        if not move.toSquare in piece.baseMovement(self.gameState.board):
            return False
        
        # checks
        self.gameState.board.movePiece(move)
        if self.gameState.board.findKing(self.gameState.isWhiteTurn) in self.gameState.board.attackMap(not self.gameState.isWhiteTurn):
            self.gameState.board.unMove(move, capturedPiece)
            return False
        else:
            self.gameState.board.unMove(move, capturedPiece)
            return True
    
    def legalMoves(self, moves):
        legalMoves = []

        for move in moves:
            if self.isLegalMove(move):
                legalMoves.append(move)
        
        return legalMoves
