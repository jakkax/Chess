import os
from PIL import Image, ImageTk

class BoardView:
    def __init__(self):
        self.boardWidth = 800
        self.boardHeight = 800

        self.originX = 0
        self.originY = 0

        self.rows = 8
        self.columns = 8

        self.pixelsInSquare = self.boardWidth // self.rows

        self.pieceScale = 1 # compared to width of square

    def renderBoard(self, canvas):
        oddColour = 'peachpuff'
        evenColour = 'darksalmon'

        for i in range(self.columns):
            for j in range(self.rows):
                colour = evenColour if (i + j) % 2 == 1 else oddColour
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

    def renderPieces(self, canvas, gameState):
        getPieceImage = {'Pawn': {True: self.whitePawn, False: self.blackPawn},
                         'Rook': {True: self.whiteRook, False: self.blackRook},
                         'Knight': {True: self.whiteKnight, False: self.blackKnight},
                         'Bishop': {True: self.whiteBishop, False: self.blackBishop},
                         'Queen': {True: self.whiteQueen, False: self.blackQueen},
                         'King': {True: self.whiteKing, False: self.blackKing}}

        for rowIndex, row in enumerate(gameState.board):
            for columnIndex, piece in enumerate(row):
                if piece is None:
                    continue

                pieceType = piece.__class__.__name__
                image = getPieceImage[pieceType][piece.colour]

                canvas.create_image((columnIndex + 0.5) * self.pixelsInSquare + self.originX, (rowIndex + 0.5) * self.pixelsInSquare + self.originY, image = image)
