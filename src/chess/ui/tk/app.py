import tkinter
from chess.core.game_state import GameState
from .input_handler import LeftClick, RightClick
from .board_view import BoardView

class App:
    def __init__(self):
        self.gameState = GameState()
        self.boardView = BoardView()
        self.leftClick = LeftClick()
        self.rightClick = RightClick()

        self.selectedPiece = None
    
    def click(self, clickCoords):
        clickedRow = (clickCoords[1] - self.boardView.originY) // self.boardView.pixelsInSquare
        clickedColumn = (clickCoords[0] - self.boardView.originX) // self.boardView.pixelsInSquare
        clickedPiece = self.gameState.board[clickedRow][clickedColumn]

        if self.selectedPiece is None:
            self.selectedPiece = clickedPiece if clickedPiece is not None and clickedPiece.isWhite == self.gameState.isWhiteTurn else None
            return
        
        # there is a selected piece
        if clickedPiece is not None and clickedPiece.isWhite == self.gameState.isWhiteTurn:
            self.selectedPiece = clickedPiece
            return

        self.gameState.board[clickedRow][clickedColumn] = self.selectedPiece
        self.gameState.board[self.selectedPiece.row][self.selectedPiece.column] = None
        
        print(self.gameState)

        self.selectedPiece = None
        self.gameState.isWhiteTurn = not self.gameState.isWhiteTurn

        self.boardView.renderPieces(self.canvas, self.gameState)

        # # there is a selected piece
        # if move(start, end) is legal:
        #     move the piece
        #     update GameState
        # else:
        #     deselect the piece

    def dragClick(self, start, end):
        pass
    
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
        self.gameState.setupBoard(True) # white pieces are down
        
        self.boardView.renderBoard(self.canvas)
        self.boardView.renderPieces(self.canvas, self.gameState)

    def run(self):
        self.setupCanvas()
        self.setupGame()

        self.canvas.mainloop()
