import os
from PIL import Image, ImageTk

class BoardView:
    def __init__(self):
        self.boardLength = 700 # in pixels # 800

        self.originX = 0
        self.originY = 0
        self.origin = (self.originX, self.originY)

        self.rows = 8
        self.columns = 8

        self.pixelsInSquare = self.boardLength // self.rows

        self.pieceScale = 1 # compared to width of square

        pieceImages = {}

    def renderBoard(self, canvas):
        lightColour = 'peachpuff'
        darkColour = 'darksalmon'

        for i in range(self.columns):
            for j in range(self.rows):
                colour = lightColour if (i + j) % 2 == 0 else darkColour
                canvas.create_rectangle((j) * self.pixelsInSquare + self.originX,
                                       (i) * self.pixelsInSquare + self.originY,
                                       (j + 1) * self.pixelsInSquare + self.originX,
                                       (i + 1) * self.pixelsInSquare + self.originY,
                                       fill = colour, width = 0)
    def loadPiece(self, piece):
        path = os.path.join(os.path.dirname(__file__), 'assets', piece)
        resized = Image.open(path).convert('RGBA').resize((int(self.pixelsInSquare * self.pieceScale), int(self.pixelsInSquare * self.pieceScale)), Image.LANCZOS)
        return ImageTk.PhotoImage(resized)

    def loadPieces(self):
        self.whitePawn = self.loadPiece('white.pawn.png')
        self.whiteRook = self.loadPiece('white.rook.png')
        self.whiteKnight = self.loadPiece('white.knight.png')
        self.whiteBishop = self.loadPiece('white.bishop.png')
        self.whiteQueen = self.loadPiece('white.queen.png')
        self.whiteKing = self.loadPiece('white.king.png')

        self.blackPawn = self.loadPiece('black.pawn.png')
        self.blackRook = self.loadPiece('black.rook.png')
        self.blackKnight = self.loadPiece('black.knight.png')
        self.blackBishop = self.loadPiece('black.bishop.png')
        self.blackQueen = self.loadPiece('black.queen.png')
        self.blackKing = self.loadPiece('black.king.png')

        self.pieceImages = {'Pawn': {True: self.whitePawn, False: self.blackPawn},
                         'Rook': {True: self.whiteRook, False: self.blackRook},
                         'Knight': {True: self.whiteKnight, False: self.blackKnight},
                         'Bishop': {True: self.whiteBishop, False: self.blackBishop},
                         'Queen': {True: self.whiteQueen, False: self.blackQueen},
                         'King': {True: self.whiteKing, False: self.blackKing}}

    def renderPieces(self, canvas, board):
        canvas.delete('piece')

        for rowIndex, row in enumerate(board):
            for columnIndex, piece in enumerate(row):
                if piece is None:
                    continue

                pieceType = piece.__class__.__name__
                image = self.pieceImages[pieceType][piece.isWhite]

                canvas.create_image((columnIndex + 0.5) * self.pixelsInSquare + self.originX,
                (rowIndex + 0.5) * self.pixelsInSquare + self.originY,
                image = image, tags = 'piece')
    
    def deselectPiece(self, canvas):
        canvas.delete('selectedPiece')
    
    def selectPiece(self, canvas, square, board):
        self.deselectPiece(canvas)

        if (square[0] + square[1]) % 2 == 0:
            colour = 'gray65' # light square
        else:
            colour = 'gray60' # dark square

        x, y = square[1] * self.pixelsInSquare, square[0] * self.pixelsInSquare
        canvas.create_rectangle(x, y, x + self.pixelsInSquare, y + self.pixelsInSquare, fill=colour, width = 0, tags='selectedPiece')

        self.renderPieces(canvas, board)
