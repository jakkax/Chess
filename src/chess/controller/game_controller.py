from chess.core.game_state import GameState
from chess.core.engine import Engine
from chess.core.move import Move
from chess.ui.tk.board_view import BoardView

class GameController:
    def __init__(self, gameState, boardView):
        self.engine = Engine(gameState)
        self.gameState = gameState
        self.boardView = boardView
        
        self.selectedPiece = None
        self.selectedSquare = ()

    def handleClick(self, clickedSquare):
        clickedPiece = self.gameState.position.board[clickedSquare[0]][clickedSquare[1]]
        # clickedPieceType = type(clickedPiece).__name__.lower()

        if self.selectedPiece is None:
            if clickedPiece is not None and clickedPiece.isWhite == self.gameState.isWhiteTurn:
                self.selectedPiece, self.selectedSquare = clickedPiece, clickedSquare
                self.boardView.selectPiece(clickedSquare, self.gameState.position.board)
                self.boardView.renderLegalMoves(self.selectedPiece.baseMovement(self.gameState.position.board)) # self.engine.legalMoves(clickedPieceType, self.gameState.board, self.selectedSquare)
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
                self.boardView.selectPiece(clickedSquare, self.gameState.position.board)
                self.boardView.renderLegalMoves(self.selectedPiece.baseMovement(self.gameState.position.board)) # self.engine.legalMoves(clickedPieceType, self.gameState.board, self.selectedSquare)
                return
        
        # the clicked square is empty / there's an enemy piece on it
        
        fromSquare = self.selectedSquare
        move = Move(fromSquare, clickedSquare) # from selected piece's square to the clicked square

        if self.engine.isLegalMove(move):
            self.gameState.applyMove(move)

            self.selectedPiece, self.selectedSquare = None, None

            self.boardView.deselectPiece()
            self.boardView.deleteLegalMoves()
            self.boardView.renderPieces(self.gameState.position.board)
        else:
            self.selectedPiece, self.selectedSquare = None, None
            self.boardView.deselectPiece()
            self.boardView.deleteLegalMoves()

    def handleDragClick(self, start, end):
        startingSquare = self.gameState.position.board[start[0]][start[1]]
        endingSquare = self.gameState.position.board[end[0]][end[1]]

        if startingSquare is None or startingSquare.isWhite != self.gameState.isWhiteTurn or (endingSquare is not None and startingSquare.isWhite == endingSquare.isWhite):
            self.handleClick(end)
