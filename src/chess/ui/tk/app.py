import tkinter

from chess.controller.game_controller import GameController
from chess.core.game_state import GameState
from .input_handler import LeftClick, RightClick
from .board_view import BoardView

class App:
    def __init__(self):
        self.gameState = GameState()
        self.boardView = BoardView()
        self.controller = GameController(self.gameState, self.boardView)
        self.leftClick = LeftClick(self.boardView.origin, self.boardView.pixelsInSquare)
        self.rightClick = RightClick(self.boardView.origin, self.boardView.pixelsInSquare)
    
    def handleClick(self, clickedSquare):
        self.controller.handleClick(clickedSquare)

    def handleDragClick(self, start, end):
        self.controller.handleDragClick(start, end)
    
    def handleRelease(self, event):
        if event.num == 1:
            self.leftClick.handleRelease(event, self.handleClick, self.handleDragClick)
        elif event.num == 3:
            self.rightClick.handleRelease(event)
    
    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width = self.boardView.boardLength, height = self.boardView.boardLength)
        self.canvas.pack()

        self.boardView.canvas = self.canvas

        self.canvas.bind('<Button-1>', self.leftClick.handleClick)
        self.canvas.bind('<B1-Motion>', self.leftClick.handleMotion)
        self.canvas.bind('<ButtonRelease-1>', self.handleRelease)

        self.canvas.bind('<Button-3>', self.rightClick.handleClick)
        self.canvas.bind('<ButtonRelease-3>', self.handleRelease)
    
    def setupGame(self):
        self.boardView.loadAssets() # loads pieces into variables
        
        self.boardView.renderBoard()
        self.boardView.renderPieces(self.gameState.position.board)

    def run(self):
        self.setupCanvas()
        self.setupGame()

        self.canvas.mainloop()
