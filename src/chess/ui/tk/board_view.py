import os
from PIL import Image, ImageTk, ImageDraw

class BoardView:
    def __init__(self, canvas = None):
        self.canvas = canvas

        self.boardLength = 800 # in pixels

        self.originX = 0
        self.originY = 0
        self.origin = (self.originX, self.originY)

        self.rows = 8
        self.columns = 8

        self.pixelsInSquare = self.boardLength // self.rows

        self.pieceScale = 1 # compared to width of square

        self.pieceImages = {}
        self.oval = None

    def renderBoard(self):
        lightColour = 'peachpuff'
        darkColour = 'darksalmon'

        for i in range(self.columns):
            for j in range(self.rows):
                colour = lightColour if (i + j) % 2 == 0 else darkColour
                self.canvas.create_rectangle((j) * self.pixelsInSquare + self.originX,
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
    
    def loadOval(self):
        size = self.pixelsInSquare // 4
        scale = 4  # draw 4× bigger

        big = Image.new("RGBA", (size*scale, size*scale), (0,0,0,0))
        draw = ImageDraw.Draw(big)

        draw.ellipse((0, 0, size*scale-1, size*scale-1), fill=(145, 145, 145))

        # downscale with high-quality resampling
        img = big.resize((size, size), Image.LANCZOS)

        self.oval = ImageTk.PhotoImage(img)
    
    def loadAssets(self):
        self.loadPieces()
        self.loadOval() # for showing legal moves

    def renderPieces(self, board):
        self.canvas.delete('piece')

        for rowIndex, row in enumerate(board):
            for columnIndex, piece in enumerate(row):
                if piece is None:
                    continue

                pieceType = piece.__class__.__name__
                image = self.pieceImages[pieceType][piece.isWhite]

                self.canvas.create_image((columnIndex + 0.5) * self.pixelsInSquare + self.originX,
                (rowIndex + 0.5) * self.pixelsInSquare + self.originY,
                image = image, tags = 'piece')
    
    def deselectPiece(self):
        self.canvas.delete('selectedPiece')
    
    def selectPiece(self, square, board):
        self.deselectPiece()

        if (square[0] + square[1]) % 2 == 0:
            colour = 'gray65' # light square
        else:
            colour = 'gray60' # dark square

        x, y = square[1] * self.pixelsInSquare, square[0] * self.pixelsInSquare
        self.canvas.create_rectangle(x, y, x + self.pixelsInSquare, y + self.pixelsInSquare, fill=colour, width = 0, tags='selectedPiece')

        self.renderPieces(board)
    
    def deleteLegalMoves(self):
        self.canvas.delete('legalMove')
    
    def renderLegalMoves(self, moves):
        self.deleteLegalMoves()

        for move in moves:
            middleX = (move[1] + 0.5) * self.pixelsInSquare
            middleY = (move[0] + 0.5) * self.pixelsInSquare

            # radius = self.pixelsInSquare / 9

            # if (move[0] + move[1]) % 2 == 0:
            #     colour = 'gray61' # light square
            # else:
            #     colour = 'gray62' # dark square

            self.canvas.create_image(middleX, middleY,
                               image = self.oval,
                               tags = 'legalMove')
