import tkinter
from chess.core.game_state import GameState
from .input_handler import InputHandler
from .board_view import BoardView

class App:
    def __init__(self):
        self.gameState = GameState()
        self.boardView = BoardView()
        self.inputHandler = InputHandler()

        self.selectedPiece = None

        self.draggingMouse = False
        self.startRow = -1
        self.startColumn = -1
    
    def handleClick(self, event):
        self.startRow, self.startColumn = self.inputHandler.handleClick(event, (self.boardView.originX, self.boardView.originY), self.boardView.pixelsInSquare)
    
    def handleMotion(self, event):
        self.draggingMouse = True
        # self.boardView.motion()

    def handleButtonRelease(self, event): # fix: differenciate between clicking and dragging!!!
        endRow, endColumn = self.inputHandler.handleClick(event, (self.boardView.originX, self.boardView.originY), self.boardView.pixelsInSquare)

        if self.startRow == endRow and self.startColumn == endColumn:
            if self.selectedPiece is None:
                self.selectedPiece = self.gameState.board[endRow][endColumn]
            else:
                pass
                # showMoves()
            return


    def setupGame(self):
        self.boardView.loadPieces() # loads pieces into variables
        self.gameState.setupboard(True) # white pieces are down
        
        self.boardView.renderBoard(self.canvas)
        self.boardView.renderPieces(self.canvas, self.gameState)
    
    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width = self.boardView.boardWidth, height = self.boardView.boardHeight)
        self.canvas.pack()
        self.canvas.bind('<Button>', self.handleClick)
        self.canvas.bind('<B1-Motion>', self.handleMotion)
        self.canvas.bind('<ButtonRelease>', self.handleButtonRelease)

    def run(self):
        self.setupCanvas()
        self.setupGame()

        self.canvas.mainloop()
