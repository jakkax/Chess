class BoardView:
    def __init__(self):
        self.rows = 8
        self.columns = 8

        self.oddColour = 'peach'
        self.evenColour = 'salmon'

    def renderBoard(self):
        for i in range(self.columns):
            for j in range(self.rows):
                colour = self.oddColour if (i + j) % 2 == 1 else self.evenColour
                print(colour)