import tkinter
from .input_handler import InputHandler
from .baord_view import BoardView

class App:
    def handleClick(self, event):
        click = event.num
        x = event.x
        y = event.y

        if click == 1:
            InputHandler.leftClick(x, y)
        else:
            InputHandler.rightClick(x, y)
    
    def setupGame(self):
        board = BoardView()
        board.renderBoard()

    def run(self):
        self.canvas = tkinter.Canvas(width = 800, height = 800)
        self.canvas.pack()
        
        self.canvas.bind('<Button>', self.handleClick)

        self.setupGame()

        self.canvas.mainloop()
