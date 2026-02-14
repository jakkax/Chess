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
    
    def clickedSquare(self, start, end):
        pass

    def dragClick(self, start, end):
        pass
    
    def handleRelease(self, event):
        if event.num == 1:
            self.leftClick.handleRelease(event, self.clickedSquare, self.dragClick)
        elif event.num == 3:
            self.rightClick.handleRelease(event)
    
    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width = self.boardView.boardWidth, height = self.boardView.boardHeight)
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
