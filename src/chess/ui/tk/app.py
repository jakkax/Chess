import tkinter
from chess.core.game_state import GameState
from .input_handler import InputHandler
from .baord_view import BoardView

class App:
    def __init__(self):
        self.gameState = GameState()
        self.board = BoardView()
        self.inputHandler = InputHandler()
    
    def handleClick(self, event):
        click = event.num
        x = event.x
        y = event.y

        if click == 1:
            self.inputHandler.leftClick(x, y)
        elif click == 3:
            self.inputHandler.rightClick(x, y)
    
    def setupGame(self):
        self.board.loadPieces()
        self.gameState.setupBoard()
        
        self.board.renderBoard(self.canvas)
        self.board.renderPieces(self.canvas, self.gameState)
    
    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width = self.board.boardWidth, height = self.board.boardHeight)
        self.canvas.pack()
        self.canvas.bind('<Button>', self.handleClick)

    def run(self):
        self.setupCanvas()
        self.setupGame()
        
        self.canvas.mainloop()
