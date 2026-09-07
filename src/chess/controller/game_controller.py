from chess.core.engine import Engine
from chess.core.move import Move

class GameController:
    def __init__(self, gameState, boardView):
        self.engine = Engine(gameState)
        self.gameState = gameState
        self.boardView = boardView
        
        self.selectedPiece = None
        self.selectedSquare = ()

    def handleClick(self, clickedSquare):
        clickedPiece = self.gameState.board.coords(clickedSquare)

        baseMovement = []
        legalMoves = []
        if self.selectedPiece:
            baseMovement = Move.tuplesToMoves((self.selectedPiece.row, self.selectedPiece.column), self.selectedPiece.baseMovement(self.gameState.board))
            legalMoves = self.engine.legalMoves(baseMovement)
        elif clickedPiece:
            baseMovement = Move.tuplesToMoves((clickedPiece.row, clickedPiece.column), clickedPiece.baseMovement(self.gameState.board))
            legalMoves = self.engine.legalMoves(baseMovement)

        if self.selectedPiece is None:
            if clickedPiece is not None and clickedPiece.isWhite == self.gameState.isWhiteTurn:
                self.selectedPiece, self.selectedSquare = clickedPiece, clickedSquare
                self.boardView.selectPiece(clickedSquare, self.gameState.board.grid)
                self.boardView.renderLegalMoves(legalMoves)
                # self.boardView.renderLegalMoves(self.selectedPiece.baseMovement(self.gameState.board)) # self.engine.legalMoves(clickedPieceType, self.gameState.board self.selectedSquare)
            return
        
        # there is a selected piece
        
        if clickedPiece is not None:
            if clickedPiece == self.selectedPiece:
                self.selectedPiece, self.selectedSquare = None, None
                self.boardView.deselectPiece()
                self.boardView.deleteLegalMoves()
                return

            if clickedPiece.isWhite == self.gameState.isWhiteTurn:
                self.selectedPiece = clickedPiece
                self.selectedSquare = clickedSquare
                self.boardView.selectPiece(clickedSquare, self.gameState.board.grid)
                self.boardView.renderLegalMoves(self.engine.legalMoves(Move.tuplesToMoves((clickedPiece.row, clickedPiece.column), clickedPiece.baseMovement(self.gameState.board))))
                # self.boardView.renderLegalMoves(self.selectedPiece.baseMovement(self.gameState.board)) # self.engine.legalMoves(clickedPieceType, self.gameState.grid, self.selectedSquare)
                return
        
        # there is a selected piece and the clicked square is empty / there's an enemy piece on it
        
        fromSquare = self.selectedSquare
        move = Move(fromSquare, clickedSquare) # from selected piece's square to the clicked square

        if self.engine.isLegalMove(move):
            self.gameState.applyMove(move)

            self.selectedPiece, self.selectedSquare = None, None

            self.boardView.deselectPiece()
            self.boardView.deleteLegalMoves()
            self.boardView.renderPieces(self.gameState.board.grid)
        else:
            self.selectedPiece, self.selectedSquare = None, None
            self.boardView.deselectPiece()
            self.boardView.deleteLegalMoves()

    def handleDragClick(self, start, end):
        startingSquare = self.gameState.board.coords(start)
        endingSquare = self.gameState.board.coords(end)

        if startingSquare is None or startingSquare.isWhite != self.gameState.isWhiteTurn or (endingSquare is not None and startingSquare.isWhite == endingSquare.isWhite):
            self.handleClick(end)
