import tkinter

#todo game end

boardWidth = 600

canvas = tkinter.Canvas(width=boardWidth, height=boardWidth)
canvas.pack()

class Chess():
    def initialise(self):
        frontend.createBoard()
        frontend.drawPieces()

class Frontend():
    def __init__(self, boardWidth):
        self.boardWidth = boardWidth
        self.pixelPerSquare = self.boardWidth/8
        self.middleOfSquares = []
        for i in range(8):
            for j in range(8):
                self.middleOfSquares.append([j*self.pixelPerSquare+self.pixelPerSquare/2, i*self.pixelPerSquare+self.pixelPerSquare/2])
        self.selectedPiece = None
        
        self.p = tkinter.PhotoImage(file='p.png')
        self.r = tkinter.PhotoImage(file='r.png')
        self.n = tkinter.PhotoImage(file='n.png')
        self.b = tkinter.PhotoImage(file='b.png')
        self.q = tkinter.PhotoImage(file='q.png')
        self.k = tkinter.PhotoImage(file='k.png')
        
        self.P = tkinter.PhotoImage(file='P1.png')
        self.R = tkinter.PhotoImage(file='R1.png')
        self.N = tkinter.PhotoImage(file='N1.png')
        self.B = tkinter.PhotoImage(file='B1.png')
        self.Q = tkinter.PhotoImage(file='Q1.png')
        self.K = tkinter.PhotoImage(file='K1.png')
    
    def createBoard(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    colour = 'peachpuff'
                else:
                    colour = 'darksalmon'
                canvas.create_rectangle(
                    i*self.pixelPerSquare, j*self.pixelPerSquare,
                    i*self.pixelPerSquare+self.pixelPerSquare, j*self.pixelPerSquare+self.pixelPerSquare,
                    fill=colour,
                    width=0)
    
    def click(self, event): # shit code
        for index in range(len(backend.thePosition)):
            if self.middleOfSquares[index][0]-self.pixelPerSquare/2 < event.x < self.middleOfSquares[index][0]+self.pixelPerSquare/2 and self.middleOfSquares[index][1]-self.pixelPerSquare/2 < event.y < self.middleOfSquares[index][1]+self.pixelPerSquare/2:
                backend.handleClick(index)
    
    def deleteSelectedPiece(self):
        canvas.delete(self.selectedPiece)
    
    def selectPiece(self, i):
        canvas.delete(self.selectedPiece)
        self.selectedPiece=canvas.create_rectangle(self.middleOfSquares[i][0]-self.pixelPerSquare/2,
                                                   self.middleOfSquares[i][1]-self.pixelPerSquare/2,
                                                   self.middleOfSquares[i][0]+self.pixelPerSquare/2,
                                                   self.middleOfSquares[i][1]+self.pixelPerSquare/2,
                                                   fill='gold2',
                                                   width=0)
        self.drawPieces()
    
    def unselectPiece(self):
        self.deleteSelectedPiece()
        canvas.delete('showMoves')
        backend.selectedPiece = None
    
    def showMoves(self, list):
        for i in list:
            canvas.create_oval(self.middleOfSquares[i][0]-self.pixelPerSquare/7,
                                self.middleOfSquares[i][1]-self.pixelPerSquare/7,
                                self.middleOfSquares[i][0]+self.pixelPerSquare/7,
                                self.middleOfSquares[i][1]+self.pixelPerSquare/7,
                                fill='gray60',
                                width=0,
                                tags='showMoves')
    
    def drawPieces(self):
        canvas.delete('p')
        canvas.delete('r')
        canvas.delete('n')
        canvas.delete('b')
        canvas.delete('q')
        canvas.delete('k')
        
        canvas.delete('P')
        canvas.delete('R')
        canvas.delete('N')
        canvas.delete('B')
        canvas.delete('Q')
        canvas.delete('K')
        
        for i in range(64):
            if backend.thePosition[i] != ' ':
                if backend.thePosition[i] == 'p':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.p, tags='p')
                elif backend.thePosition[i] == 'r':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.r, tags='r')
                elif backend.thePosition[i] == 'n':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.n, tags='n')
                elif backend.thePosition[i] == 'b':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.b, tags='b')
                elif backend.thePosition[i] == 'q':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.q, tags='q')
                elif backend.thePosition[i] == 'k':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.k, tags='k')
                elif backend.thePosition[i] == 'P':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.P, tags='P')
                elif backend.thePosition[i] == 'R':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.R, tags='R')
                elif backend.thePosition[i] == 'N':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.N, tags='N')
                elif backend.thePosition[i] == 'B':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.B, tags='B')
                elif backend.thePosition[i] == 'Q':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.Q, tags='Q')
                elif backend.thePosition[i] == 'K':
                    canvas.create_image(self.middleOfSquares[i][0], self.middleOfSquares[i][1], image=self.K, tags='K')

# class Piece():
#     def __init__(column, row)
#         self.position = [column, row]
#     
# class King(Piece):
#     def __init__(isWhite)
#         self.isWhite = isWhite
#         self.moved = false
# 
# blackKing = King(False)
class Backend():
    def __init__(self):
#         self.board = [blackKing, None, None]
        self.thePosition = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
                           'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                           'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
                           'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.selectedPiece = None
        self.isColour = ['P', 'R', 'N', 'B', 'Q', 'K']
        self.notColour = ['p', 'r', 'n', 'b', 'q', 'k']
        self.enPassantPossible = False
        self.lastMove = None
        self.takePiece = None
        
        self.whiteKingNotMoved = True
        self.blackKingNotMoved = True
        self.whiteLeftRookNotMoved = True
        self.whiteRightRookNotMoved = True
        self.blackLeftRookNotMoved = True
        self.blackRightRookNotMoved = True
    
    def movePiece(self, index):
        if self.thePosition[self.selectedPiece] == 'P':
            if 7 >= index:
                self.thePosition[index] = 'Q'
            else:
                self.thePosition[index] = self.thePosition[self.selectedPiece]
            self.thePosition[self.selectedPiece] = ' '
            
            if self.selectedPiece-index == 9 and self.takePiece == -1:
                self.thePosition[self.selectedPiece+self.takePiece] = ' '
                self.takePiece = None
            elif self.selectedPiece-index == 7 and self.takePiece == 1:
                self.thePosition[self.selectedPiece+self.takePiece] = ' '
                self.takePiece = None
            
            if self.selectedPiece-index == 16:
                self.enPassantPossible = True
            else:
                self.enPassantPossible = False
        elif self.thePosition[self.selectedPiece] == 'p':
            if index >= 56:
                self.thePosition[index] = 'q'
            else:
                self.thePosition[index] = self.thePosition[self.selectedPiece]
            self.thePosition[self.selectedPiece] = ' '
            
            if self.selectedPiece-index == -9 and self.takePiece == 1:
                self.thePosition[self.selectedPiece+self.takePiece] = ' '
                self.takePiece = None
            elif self.selectedPiece-index == -7 and self.takePiece == -1:
                self.thePosition[self.selectedPiece+self.takePiece] = ' '
                self.takePiece = None
            
            if index-self.selectedPiece == 16:
                self.enPassantPossible = True
            else:
                self.enPassantPossible = False
        else:
            self.thePosition[index] = self.thePosition[self.selectedPiece]
            self.thePosition[self.selectedPiece] = ' '
            self.enPassantPossible = False
            
            if (self.thePosition[index] == 'K' or self.thePosition[index] == 'k') and self.selectedPiece-index == -2:
                if self.thePosition[7] in self.isColour and self.thePosition[7] == 'r':
                    self.thePosition[7], self.thePosition[5] = self.thePosition[5], self.thePosition[7]
                elif self.thePosition[63] in self.isColour and self.thePosition[63] == 'R':
                    self.thePosition[63], self.thePosition[61] = self.thePosition[61], self.thePosition[63]
            if (self.thePosition[index] == 'K' or self.thePosition[index] == 'k') and self.selectedPiece-index == 2:
                if self.thePosition[0] in self.isColour and self.thePosition[0] == 'r':
                    self.thePosition[0], self.thePosition[3] = self.thePosition[3], self.thePosition[0]
                elif self.thePosition[56] in self.isColour and self.thePosition[56] == 'R':
                    self.thePosition[56], self.thePosition[59] = self.thePosition[59], self.thePosition[56]
            
            if self.thePosition[index] == 'K':
                self.whiteKingNotMoved = False
            elif self.thePosition[index] == 'k':
                self.blackKingNotMoved = False
            
            if self.thePosition[index] == 'R':
                if self.selectedPiece == 56:
                    self.whiteLeftRookNotMoved = False
                elif self.selectedPiece == 63:
                    self.whiteRightRookNotMoved = False
            elif self.thePosition[index] == 'r':
                if self.selectedPiece == 0:
                    self.blackLeftRookNotMoved = False
                elif self.selectedPiece == 7:
                    self.blackRightRookNotMoved = False
            elif index == 56:
                self.whiteLeftRookNotMoved = False
            elif index == 63:
                self.whiteRightRookNotMoved = False
            elif index == 0:
                self.blackLeftRookNotMoved = False
            elif index == 7:
                self.blackRightRookNotMoved = False
        self.isColour, self.notColour = self.notColour, self.isColour
        self.lastMove = index
        frontend.drawPieces()
    
    def pawnLegalMoves(self, onlyCaptures=False):
        x = []
        
        if onlyCaptures:
            if self.thePosition[self.selectedPiece] == 'P':
                if self.selectedPiece-7 > 0:
                    if self.selectedPiece%8 == 0:
                        x.append(self.selectedPiece-7)
                    if (self.selectedPiece+1)%8 == 0:
                        x.append(self.selectedPiece-9)
                    else:
                        x.append(self.selectedPiece-7)
                        x.append(self.selectedPiece-9)
            else:
                if self.selectedPiece+7 < 63:
                    if self.selectedPiece%8 == 0:
                        x.append(self.selectedPiece+9)
                    if (self.selectedPiece+1)%8 == 0:
                        x.append(self.selectedPiece+7)
                    else:
                        x.append(self.selectedPiece+7)
                        x.append(self.selectedPiece+9)
            return x
        
        if self.thePosition[self.selectedPiece] == 'P':
            if self.selectedPiece-7 >= 0:
                if self.selectedPiece%8 == 0:
                    if self.thePosition[self.selectedPiece-7] in self.notColour:
                        x.append(self.selectedPiece-7)
                elif (self.selectedPiece+1)%8 == 0:
                    if self.thePosition[self.selectedPiece-9] in self.notColour:
                        x.append(self.selectedPiece-9)
                else:
                    if self.thePosition[self.selectedPiece-7] in self.notColour:
                        x.append(self.selectedPiece-7)
                    if self.thePosition[self.selectedPiece-9] in self.notColour:
                        x.append(self.selectedPiece-9)
            
            if self.thePosition[self.selectedPiece-8] == ' ':
                x.append(self.selectedPiece-8)
                if 48 <= self.selectedPiece <= 55 and self.thePosition[self.selectedPiece-16] == ' ':
                    x.append(self.selectedPiece-16)
            
            if self.thePosition[self.selectedPiece-1] == 'p' and self.enPassantPossible and self.lastMove == self.selectedPiece-1 and 24 <= self.selectedPiece <= 31: # en passant
                x.append(self.selectedPiece-9)
                self.takePiece = -1
            elif self.thePosition[self.selectedPiece+1] == 'p' and self.enPassantPossible and self.lastMove == self.selectedPiece+1 and 24 <= self.selectedPiece <= 31:
                x.append(self.selectedPiece-7)
                self.takePiece = 1
        
        else:
            if self.selectedPiece+7 <= 63:
                if self.selectedPiece%8 == 0:
                    if self.thePosition[self.selectedPiece+9] in self.notColour:
                        x.append(self.selectedPiece+9)
                elif (self.selectedPiece+1)%8 == 0:
                    if self.thePosition[self.selectedPiece+7] in self.notColour:
                        x.append(self.selectedPiece+7)
                else:
                    if self.thePosition[self.selectedPiece+7] in self.notColour:
                        x.append(self.selectedPiece+7)
                    if self.thePosition[self.selectedPiece+9] in self.notColour:
                        x.append(self.selectedPiece+9)
            
            if self.thePosition[self.selectedPiece+8] == ' ':
                x.append(self.selectedPiece+8)
                if 8 <= self.selectedPiece <= 15 and self.thePosition[self.selectedPiece+16] == ' ':
                    x.append(self.selectedPiece+16)
            
            if self.thePosition[self.selectedPiece-1] == 'P' and self.enPassantPossible and self.lastMove == self.selectedPiece-1 and 32 <= self.selectedPiece <= 39: # en passant
                x.append(self.selectedPiece+7)
                self.takePiece = -1
            elif self.thePosition[self.selectedPiece+1] == 'P' and self.enPassantPossible and self.lastMove == self.selectedPiece+1 and 32 <= self.selectedPiece <= 39:
                x.append(self.selectedPiece+9)
                self.takePiece = 1
        
        return x
    
    def rookLegalMoves(self):
        x = []
        
        i = self.selectedPiece
        while i-8 >= 0:
            if self.thePosition[i-8] in self.isColour:
                break
            if self.thePosition[i-8] in self.notColour:
                x.append(i-8)
                break
            x.append(i-8)
            i -= 8
        
        i = self.selectedPiece
        while i+8 <= 63:
            if self.thePosition[i+8] in self.isColour:
                break
            if self.thePosition[i+8] in self.notColour:
                x.append(i+8)
                break
            x.append(i+8)
            i += 8
        
        i = self.selectedPiece
        while i % 8 != 0:
            if self.thePosition[i-1] in self.isColour:
                break
            if self.thePosition[i-1] in self.notColour:
                x.append(i-1)
                break
            x.append(i-1)
            i -= 1
        
        i = self.selectedPiece
        while (i+1) % 8 != 0:
            if self.thePosition[i+1] in self.isColour:
                break
            if self.thePosition[i+1] in self.notColour:
                x.append(i+1)
                break
            x.append(i+1)
            i += 1
        
        return x
    
    def knightLegalMoves(self):
        x = []
        i = self.selectedPiece
        knightMoves = [10, -6, -15, 17, -17, 15, 6, -10]
        
        if (i-6)%8 == 0:
            knightMoves = knightMoves[2::]
        elif (i-7)%8 == 0:
            knightMoves = knightMoves[4::]
        elif (i-1)%8 == 0:
            knightMoves = knightMoves[0:6]
        elif i%8 == 0:
            knightMoves = knightMoves[0:4]
        
        for j in knightMoves:
            if j > 0:
                if i+j <= 63:
                    if self.thePosition[i+j] not in self.isColour:
                        x.append(i+j)
            else:
                if i+j >= 0:
                    if self.thePosition[i+j] not in self.isColour:
                        x.append(i+j)
        
        return x
    
    def bishopLegalMoves(self):
        x = []
        
        i = self.selectedPiece
        while i-7 >= 0 and (i+1) % 8 != 0:
            if self.thePosition[i-7] in self.isColour:
                break
            if self.thePosition[i-7] in self.notColour:
                x.append(i-7)
                break
            x.append(i-7)
            i -= 7
        
        i = self.selectedPiece
        while i+7 <= 63 and i % 8 != 0:
            if self.thePosition[i+7] in self.isColour:
                break
            if self.thePosition[i+7] in self.notColour:
                x.append(i+7)
                break
            x.append(i+7)
            i += 7
        
        i = self.selectedPiece
        while i-9 >= 0 and i % 8 != 0:
            if self.thePosition[i-9] in self.isColour:
                break
            if self.thePosition[i-9] in self.notColour:
                x.append(i-9)
                break
            x.append(i-9)
            i -= 9
        
        i = self.selectedPiece
        while i+9 <= 63 and (i+1) % 8 != 0:
            if self.thePosition[i+9] in self.isColour:
                break
            if self.thePosition[i+9] in self.notColour:
                x.append(i+9)
                break
            x.append(i+9)
            i += 9
        
        return x
    
    def queenLegalMoves(self):
        return self.rookLegalMoves() + self.bishopLegalMoves()
    
    def castlingPossible(self, firstIteration=True):
        if self.thePosition[self.selectedPiece] == 'K':
            if self.whiteKingNotMoved:
                if firstIteration:
                    # left-side castling
                    if self.thePosition[61] == ' ' and self.thePosition[62] == ' ' and self.whiteRightRookNotMoved:
                        if 60 in self.calculateAllMoves([]): # !!!BUG king cannot move througe a check (or end up in one)
                            pass
                        elif 61 in self.calculateAllMoves([]):
                            pass
                        else:
                            return 62
                else:
                    # right-side castling
                    if self.thePosition[59] == ' ' and self.thePosition[58] == ' ' and self.thePosition[57] == ' ' and self.whiteLeftRookNotMoved:
                        if 60 in self.calculateAllMoves([]):
                            pass
                        elif 59 in self.calculateAllMoves([]):
                            pass
                        else:
                            return 58
        else:
            if self.blackKingNotMoved:
                if firstIteration:
                    # left-side castling
                    if self.thePosition[5] == ' ' and self.thePosition[6] == ' ' and self.blackRightRookNotMoved:
                        if 5 in self.calculateAllMoves([]):
                            pass
                        elif 6 in self.calculateAllMoves([]):
                            pass
                        else:
                            return 6
                else:                
                    # right-side castling
                    if self.thePosition[3] == ' ' and self.thePosition[2] == ' ' and self.thePosition[1] == ' ' and self.blackLeftRookNotMoved:
                        if 3 in self.calculateAllMoves([]):
                            pass
                        elif 2 in self.calculateAllMoves([]):
                            pass
                        else:
                            return 2
    
    def kingLegalMoves(self, castling=True):
        x = []
        i = self.selectedPiece
        kingMoves = [-9, -1, 7, -8, 8, -7, 1, 9]
        
        if i%8 == 0:
            kingMoves = kingMoves[3::]
        elif (i+1)%8 == 0:
            kingMoves = kingMoves[0:5]
        
        for j in kingMoves:
            if 0 <= i+j <= 63:
                if self.thePosition[i+j] not in self.isColour:
                    x.append(i+j)
        
        if castling:
            if self.castlingPossible():
                x.append(self.castlingPossible())
            if self.castlingPossible(False):
                x.append(self.castlingPossible(False))
        
        return x
    
    def updateBoard(self, index):
        if self.thePosition[self.selectedPiece] == 'p':
            if index >= 56:
                self.thePosition[index] = 'q'
            else:
                self.thePosition[index] = self.thePosition[self.selectedPiece]
            
            if self.takePiece != None:
                self.thePosition[self.selectedPiece+self.takePiece] = ' '
            
            self.thePosition[self.selectedPiece] = ' '
        elif self.thePosition[self.selectedPiece] == 'P':
            if 7 >= index:
                self.thePosition[index] = 'Q'
            else:
                self.thePosition[index] = self.thePosition[self.selectedPiece]
            
            if self.takePiece != None:
                self.thePosition[self.selectedPiece+self.takePiece] = ' '
            
            self.thePosition[self.selectedPiece] = ' '
        else:
            self.thePosition[index] = self.thePosition[self.selectedPiece]
            self.thePosition[self.selectedPiece] = ' '
            
            if (self.thePosition[index] == 'K' or self.thePosition[index] == 'k') and self.selectedPiece-index == -2:
                if self.thePosition[7] in self.isColour and self.thePosition[7] == 'r':
                    self.thePosition[7], self.thePosition[5] = self.thePosition[5], self.thePosition[7]
                elif self.thePosition[63] in self.isColour and self.thePosition[63] == 'R':
                    self.thePosition[63], self.thePosition[61] = self.thePosition[61], self.thePosition[63]
            if (self.thePosition[index] == 'K' or self.thePosition[index] == 'k') and self.selectedPiece-index == 2:
                if self.thePosition[0] in self.isColour and self.thePosition[0] == 'r':
                    self.thePosition[0], self.thePosition[3] = self.thePosition[3], self.thePosition[0]
                elif self.thePosition[56] in self.isColour and self.thePosition[56] == 'R':
                    self.thePosition[56], self.thePosition[59] = self.thePosition[59], self.thePosition[56]
    
    def calculateAllMoves(self, x):
        remember1 = self.selectedPiece
        remember = self.thePosition.copy()
        self.isColour, self.notColour = self.notColour, self.isColour
        
        for i in range(64):
            if self.thePosition[i] in self.isColour and (self.thePosition[i] == 'p' or self.thePosition[i] == 'P'):
                self.selectedPiece = i
                x.append(self.pawnLegalMoves(True)) # pawns can only capture sideways
            elif self.thePosition[i] in self.isColour and (self.thePosition[i] == 'r' or self.thePosition[i] == 'R'):
                self.selectedPiece = i
                x.append(self.rookLegalMoves())
            elif self.thePosition[i] in self.isColour and (self.thePosition[i] == 'n' or self.thePosition[i] == 'N'):
                self.selectedPiece = i
                x.append(self.knightLegalMoves())
            elif self.thePosition[i] in self.isColour and (self.thePosition[i] == 'b' or self.thePosition[i] == 'B'):
                self.selectedPiece = i
                x.append(self.bishopLegalMoves())
            elif self.thePosition[i] in self.isColour and (self.thePosition[i] == 'q' or self.thePosition[i] == 'Q'):
                self.selectedPiece = i
                x.append(self.queenLegalMoves())
            elif self.thePosition[i] in self.isColour and (self.thePosition[i] == 'k' or self.thePosition[i] == 'K'):
                self.selectedPiece = i
                x.append(self.kingLegalMoves(False))
            self.thePosition = remember.copy()
        
        self.isColour, self.notColour = self.notColour, self.isColour
        self.selectedPiece = remember1
        
        return x
    
    def allMoves(self, element): # element is the destination of the selected piece
        x = []
        remember = self.thePosition.copy()
        self.updateBoard(element)
        
        for i in range(64):
            if self.thePosition[i] in self.isColour and (self.thePosition[i] == 'k' or self.thePosition[i] == 'K'):
                kingIndex = i
        
        x = self.calculateAllMoves(x)
        self.thePosition = remember.copy()
        
        for i in x:
            if kingIndex in i:
                return False
        return True
    
    def findChecks(self, x): # x is a list of all legal moves before accounting for checks
        y = []
        
        for element in x:
            if self.allMoves(element):
                y.append(element)
        
        return y
    
    def legalMoves(self):
        x = []
        
        if self.thePosition[self.selectedPiece] == 'p' or self.thePosition[self.selectedPiece] == 'P':
            x = self.findChecks(self.pawnLegalMoves())
        
        if self.thePosition[self.selectedPiece] == 'r' or self.thePosition[self.selectedPiece] == 'R':
            x = self.findChecks(self.rookLegalMoves())
        
        if self.thePosition[self.selectedPiece] == 'n' or self.thePosition[self.selectedPiece] == 'N':
            x = self.findChecks(self.knightLegalMoves())
        
        if self.thePosition[self.selectedPiece] == 'b' or self.thePosition[self.selectedPiece] == 'B':
            x = self.findChecks(self.bishopLegalMoves())
        
        if self.thePosition[self.selectedPiece] == 'q' or self.thePosition[self.selectedPiece] == 'Q':
            x = self.findChecks(self.queenLegalMoves())
        
        if self.thePosition[self.selectedPiece] == 'k' or self.thePosition[self.selectedPiece] == 'K':
            x = self.findChecks(self.kingLegalMoves())
        
        return x
    
    def handleClick(self, index):
        if self.thePosition[index] != ' ': # if click is on a piece
            if self.selectedPiece == None: # if there is no selected piece
                if self.thePosition[index] in self.isColour: # if it is on the right colour
                    self.selectedPiece = index
                    frontend.selectPiece(index)
                    frontend.showMoves(self.legalMoves())
            else: # if there is a selected piece
                if self.selectedPiece == index: # if it is the same piece
                    frontend.unselectPiece()
                else: # if it is a different piece
                    if self.thePosition[index] in self.isColour: # if the clicked piece is in the same colour
                        frontend.unselectPiece()
                        self.selectedPiece = index
                        frontend.selectPiece(index)
                        frontend.showMoves(self.legalMoves())
                    else: # if the clicked piece is on the opposite colour
                        if index in backend.legalMoves(): # if the move is legal
                            self.movePiece(index)
                            frontend.unselectPiece()
                        else: # if the move is not legal
                            frontend.unselectPiece()
        else: # if click is on an empty square
            if self.selectedPiece == None: # if there is no selected piece
                pass
            else: # if there is a selected piece
                if index in self.legalMoves(): # if the move is legal
                    self.movePiece(index)
                    frontend.unselectPiece()
                else: # if the move is not legal
                    frontend.unselectPiece()

chess = Chess()
frontend = Frontend(boardWidth)
backend = Backend()

canvas.bind("<Button-1>", frontend.click)

chess.initialise()

canvas.mainloop()