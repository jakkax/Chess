import tkinter
from chess.core.game_state import GameState
from .input_handler import InputHandler
from .board_view import BoardView

class App:
    def __init__(self):
        self.gameState = GameState()
        self.board = BoardView()
        self.inputHandler = InputHandler()
    
    def setupGame(self):
        self.board.loadPieces()
        self.gameState.setupBoard()
        
        self.board.renderBoard(self.canvas)
        self.board.renderPieces(self.canvas, self.gameState)
    
    def handleClick(self, event):
        self.inputHandler.handleClick(event, (self.board.originX, self.board.originY), self.board.pixelsInSquare)

    def handleButtonRelease(self, event):
        pass
    
    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width = self.board.boardWidth, height = self.board.boardHeight)
        self.canvas.pack()
        self.canvas.bind('<Button>', self.handleClick)
        self.canvas.bind('<ButtonRelease>', self.handleButtonRelease)

    def run(self):
        self.setupCanvas()
        self.setupGame()
        
        self.canvas.mainloop()
