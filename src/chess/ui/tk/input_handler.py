class InputHandler:
    def leftClick(x, y):
        print('left click')
        print(x, y)

    def rightClick(x, y):
        print('right click')
        print(x, y)


    # def leftClick(self, click):
    #     row = int(click.y // frontend.pixelsInSquare)
    #     column = int(click.x // frontend.pixelsInSquare)

    #     if self.promotion:
    #         self.promote(row, column)
    #         return

    #     clickedSquare = self.board[row][column]
        
    #     frontend.deleteHighlightedSquares()
    #     frontend.highlightedSquares = []
    #     frontend.deleteArrows()
    #     frontend.arrows = []
    #     if self.gameEnded:
    #         frontend.canvas.delete('gameEnd')
    #         return
        
    #     if not self.isWhiteTurn:
    #         return
        
    #     if clickedSquare is None:
    #         if self.selectedPiece is None:
    #             return
    #         if (row, column) in self.selectedPiece.legalMoves(self.board, self.lastMovedPieces):
    #             self.movePiece(self.selectedPiece, (row, column), promotion = True)
    #             # self.selectedPiece.move(self.board, (row, column), promotion = True)
    #             if not(self.gameEnded or self.promotion):
    #                 self.getBotMove()
    #         else:
    #             self.deselectPiece()
    #         return
        
    #     if self.selectedPiece is None and clickedSquare.isWhite != self.isWhiteTurn:
    #         return
        
    #     if self.selectedPiece is None or self.selectedPiece.isWhite == clickedSquare.isWhite:
    #         if self.selectedPiece == clickedSquare:
    #             self.deselectPiece()
    #             return
            
    #         self.selectedPiece = clickedSquare
    #         frontend.selectPiece(row, column)
    #         frontend.viewLegalMoves(self.selectedPiece.legalMoves(self.board, self.lastMovedPieces))
    #     else:
    #         if (row, column) in self.selectedPiece.legalMoves(self.board, self.lastMovedPieces):
    #             self.movePiece(self.selectedPiece, (row, column), promotion = True)
    #             # self.selectedPiece.move(self.board, (row, column), promotion = True)
    #             if not(self.gameEnded or self.promotion):
    #                 self.getBotMove()
    #         else:
    #             self.deselectPiece()

    # def rightClick(self):
    #     if self.gameEnded:
    #         return
        
    #     rightClickEndPos = (int(click.y // frontend.pixelsInSquare), int(click.x // frontend.pixelsInSquare))
        
    #     if self.rightClickStartPos == rightClickEndPos:
    #         if rightClickEndPos in frontend.highlightedSquares:
    #             frontend.highlightedSquares.remove(rightClickEndPos)
    #         else:
    #             frontend.highlightedSquares.append(rightClickEndPos)
    #         frontend.drawHighlightedSquares(frontend.highlightedSquares)
    #     else:
    #         if (self.rightClickStartPos, rightClickEndPos) in frontend.arrows:
    #             frontend.arrows.remove((self.rightClickStartPos, rightClickEndPos))
    #         else:
    #             frontend.arrows.append((self.rightClickStartPos, rightClickEndPos))
    #         frontend.drawArrows()
