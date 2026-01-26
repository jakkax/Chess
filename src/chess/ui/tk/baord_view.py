import os
from PIL import Image, ImageTk

class BoardView:
    def __init__(self):
        self.boardWidth = 800
        self.boardHeight = 800

        self.rows = 8
        self.columns = 8

        self.pixelsInSquare = self.boardWidth / self.rows

    def renderBoard(self, canvas):
        oddColour = 'peachpuff'
        evenColour = 'darksalmon'

        for i in range(self.columns):
            for j in range(self.rows):
                colour = evenColour if (i + j) % 2 == 1 else oddColour
                canvas.create_rectangle(j * self.pixelsInSquare,
                                       i * self.pixelsInSquare,
                                       (j + 1) * self.pixelsInSquare,
                                       (i + 1) * self.pixelsInSquare,
                                       fill = colour, width = 0)
    
    def renderPieces(self, canvas):
        basePath = os.path.dirname(__file__)

        realPath = os.path.join(basePath, 'assets', 'white-rook.png')
        
        resized = Image.open(realPath)
        daRook = ImageTk.PhotoImage(resized)
        
        canvas.create_rectangle(0, 0, 200, 200, fill = 'red', width = 0)
        canvas.create_image(100, 100, image = daRook)
