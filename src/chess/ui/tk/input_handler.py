class InputHandler:
    def __init__(self):
        self.startClickX = -1
        self.startClickY = -1
        self.isButtonPressed = False

        self.dragging = False
        self.draggingThreshold = 3 # mouse needs to move x pixels for the click to be considered a drag

class LeftClick(InputHandler):
    def __init__(self):
        super().__init__()
    
    def handleClick(self, event):
        self.isButtonPressed = True
        self.startClickX = event.x
        self.startClickY = event.y

    def handleMotion(self, event):
        if self.isButtonPressed and (abs(self.startClickX - event.x) > self.draggingThreshold) or (abs(self.startClickY - event.y) > self.draggingThreshold):
            self.dragging = True

    def handleRelease(self, event, click, drag):
        start = (self.startClickX, self.startClickY)
        end = (event.x, event.y)

        if self.dragging:
            drag(start, end)
        else:
            click(start, end)

class RightClick(InputHandler):
    def __init__(self):
        super().__init__()
    
    def handleClick(self, event):
        self.startClickX = event.x
        self.startClickY = event.y

    def handleRelease(self, event):
        start = (self.startClickX, self.startClickY)
        end = (event.x, event.y)

#     row = (y - origin[1]) // squareSize
#     column = (x - origin[0]) // squareSize
