class InputHandler:
    # def leftClick(self, event, origin, squareSize):
    #     x = event.x
    #     y = event.y

    #     row = (y - origin[1]) // squareSize
    #     column = (x - origin[0]) // squareSize

    #     return row, column
    
    # def leftClickRelease(self, event, origin, squareSize):
    #     pass

    # def rightClick(self, event, origin, squareSize):
    #     x = event.x
    #     y = event.y

    #     row = (y - origin[1]) // squareSize
    #     column = (x - origin[0]) // squareSize

    #     return row, column

    # def rightClickRelease(self, event, origin, squareSize):
    #     pass
    
    def handleClick(self, event, origin, squareSize):
        x = event.x
        y = event.y

        row = (y - origin[1]) // squareSize
        column = (x - origin[0]) // squareSize

        return row, column
    
        # if event.num == 1:
        #     return self.leftClick(event, origin, squareSize)
        # elif event.num == 3:
        #     return self.rightClick(event, origin, squareSize)
    
    def handleButtonRelease(self, event, origin, squareSize):
        x = event.x
        y = event.y

        row = (y - origin[1]) // squareSize
        column = (x - origin[0]) // squareSize

        return row, column
    
        # if event.num == 1:
        #     self.leftClickRelease(event, origin, squareSize)
        # elif event.num == 3:
        #     self.rightClickRelease(event, origin, squareSize)
