import tkinter
from chess.core.game_state import GameState
from chess.core.board import Board
from chess.core.engine import Engine
from chess.core.move import Move
from .input_handler import LeftClick, RightClick
from .board_view import BoardView

class App:
    def __init__(self):
        self.gameState = GameState()
        self.board = Board()
        self.engine = Engine()
        self.boardView = BoardView()
        self.leftClick = LeftClick(self.boardView.origin, self.boardView.pixelsInSquare)
        self.rightClick = RightClick(self.boardView.origin, self.boardView.pixelsInSquare)

        self.selectedPiece = None
    
    def click(self, clickedSquare):
        clickedRow, clickedColumn = clickedSquare
        clickedPiece = self.board.board[clickedRow][clickedColumn]

        if self.selectedPiece is None:
            if clickedPiece is not None and clickedPiece.isWhite == self.gameState.isWhiteTurn:
                self.selectedPiece = clickedPiece
                print(self.selectedPiece.pseudoLegalMoves(self.board.board))
                self.boardView.selectPiece(self.canvas, clickedSquare, self.board.board)
            return
        
        # there is a selected piece
        
        if clickedPiece is not None:
            if clickedPiece == self.selectedPiece:
                self.selectedPiece = None
                self.boardView.deselectPiece(self.canvas)
                return

            if clickedPiece.isWhite == self.gameState.isWhiteTurn:
                self.selectedPiece = clickedPiece
                print(self.selectedPiece.pseudoLegalMoves(self.board.board))
                self.boardView.selectPiece(self.canvas, clickedSquare, self.board.board)
                return
        
        # the clicked square is empty / there's an enemy piece on it
        
        fromSquare = (self.selectedPiece.row, self.selectedPiece.column)
        move = Move(fromSquare, clickedSquare) # from selected piece's square to the clicked square

        if self.engine.isLegalMove(move, self.board.board):
            self.gameState.applyMove(move, self.board.board)

            # TODO: move this code somewhere else
            self.selectedPiece.row = clickedRow
            self.selectedPiece.column = clickedColumn
            self.selectedPiece = None

            self.boardView.deselectPiece(self.canvas)
            self.boardView.renderPieces(self.canvas, self.board.board)
        else:
            self.selectedPiece = None
            self.boardView.deselectPiece(self.canvas)

    def dragClick(self, start, end):
        startingSquare = self.board.board[start[0]][start[1]]
        endingSquare = self.board.board[end[0]][end[1]]

        if startingSquare is None or startingSquare.isWhite != self.gameState.isWhiteTurn or (endingSquare is not None and startingSquare.isWhite == endingSquare.isWhite):
            self.click(end)
    
    def handleRelease(self, event):
        if event.num == 1:
            self.leftClick.handleRelease(event, self.click, self.dragClick)
        elif event.num == 3:
            self.rightClick.handleRelease(event)
    
    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width = self.boardView.boardLength, height = self.boardView.boardLength)
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.leftClick.handleClick)
        self.canvas.bind('<B1-Motion>', self.leftClick.handleMotion)
        self.canvas.bind('<ButtonRelease-1>', self.handleRelease)

        self.canvas.bind('<Button-3>', self.rightClick.handleClick)
        self.canvas.bind('<ButtonRelease-3>', self.handleRelease)
    
    def setupGame(self):
        self.boardView.loadPieces() # loads pieces into variables
        self.board.setupBoard()
        
        self.boardView.renderBoard(self.canvas)
        self.boardView.renderPieces(self.canvas, self.board.board)

    def run(self):
        self.setupCanvas()
        self.setupGame()

        self.canvas.mainloop()
