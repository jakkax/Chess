class InputHandler:
    def __init__(self, boardOrigin, pixelsInSquare):
        self.origin = boardOrigin
        self.pixelsInSquare = pixelsInSquare

        self.startClickX = -1
        self.startClickY = -1

        self.dragging = False
        self.draggingThreshold = 3 # mouse needs to move x pixels for the click to be considered a drag
    
    def pixelsToIndices(self, x, y):
        return ((y - self.origin[1]) // self.pixelsInSquare,
                 (x - self.origin[0]) // self.pixelsInSquare)

class LeftClick(InputHandler):
    def __init__(self, boardOrigin, pixelsInSquare):
        super().__init__(boardOrigin, pixelsInSquare)
    
    def handleClick(self, event):
        self.startClickX = event.x
        self.startClickY = event.y

    def handleMotion(self, event):
        if abs(self.startClickX - event.x) > self.draggingThreshold or abs(self.startClickY - event.y) > self.draggingThreshold:
            self.dragging = True
        
        # if self.dragging:
        #     move the dragged piece

    def handleRelease(self, event, click, drag):
        start = self.pixelsToIndices(self.startClickX, self.startClickY)
        end = self.pixelsToIndices(event.x, event.y)

        if self.dragging:
            drag(start, end) # start != end
        else:
            click(end) # start == end

class RightClick(InputHandler):
    def __init__(self, boardOrigin, pixelsInSquare):
        super().__init__(boardOrigin, pixelsInSquare)
    
    def handleClick(self, event):
        self.startClickX = event.x
        self.startClickY = event.y

    def handleRelease(self, event):
        start = (self.startClickX, self.startClickY)
        end = (event.x, event.y)
