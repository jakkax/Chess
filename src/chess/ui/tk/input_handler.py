class InputHandler:
    def __init__(self):
        self.leftClickHeld = False
        self.rightClickHeld = False

    def leftClick(self, x, y, origin, squareSize):
        self.leftClickHeld = True

        row = (y - origin[1]) // squareSize
        column = (x - origin[0]) // squareSize

        return row, column
    
    def leftClickRelease(self, x, y, origin, squareSize):
        self.leftClickHeld = False

    def rightClick(self, x, y, origin, squareSize):
        self.rightClickHeld = True

        row = (y - origin[1]) // squareSize
        column = (x - origin[0]) // squareSize

    def rightClickRelease(self, x, y, origin, squareSize):
        self.rightClickHeld = False
    
    def handleClick(self, event, origin, squareSize):
        button = event.num
        x = event.x
        y = event.y

        if button == 1:
            self.leftClick(x, y, origin, squareSize)
        elif button == 3:
            self.rightClick(x, y, origin, squareSize)
    
    def handleButtonRelease(self, event, origin, squareSize):
        button = event.num
        x = event.x
        y = event.y

        if button == 1:
            self.leftClickRelease(x, y, origin, squareSize)
        elif button == 3:
            self.rightClickRelease(x, y, origin, squareSize)
