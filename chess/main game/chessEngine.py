class gamestate():
    def __init__(self):
        #2d list of board
        self.board =[["bR","bN","bB","bQ","bK","bB","bN","bR"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wR","wN","wB","wQ","wK","wB","wN","wR"],]

        self.whiteToMove =True
        self.moveLog = []
        
    def makeMove(self, move):
        if self.board[move.startRow][move.startCol] != '--':
            self.board[move.startRow][move.startCol] = '--'
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move)
            self.whiteToMove = not self.whiteToMove
        
    def undoMove(self):
        if len(self.moveLog)!=0:
            move=self.moveLog.pop()
            self.board[move.startRow][move.startCol]=move.pieceMoved
            self.board[move.endRow][move.endCol]= move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
    
    
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if(turn=='w' and self.whiteToMove) or (turn =='b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece=='p':
                        self.getPawnMoves(r,c,moves)
                    elif piece == 'R':
                        self.getRookMoves(r,c,moves)
                    elif piece=='N':
                        self.getKnightMoves(r,c,moves)
                    elif piece == 'Q':
                        self.getQueenMoves(r,c,moves)
                    elif piece=='B':
                        self.getBishopMoves(r,c,moves)
                    elif piece == 'K':
                        self.getKingMoves(r,c,moves)
        return moves
    
    
    def getPawnMoves(self,r,c,moves):
        if self.whiteToMove:
            if self.board[r-1][c]=="--":
                moves.append(Move((r,c),(r-1,c),self.board))
                if r==6 and self.board[r-2][c]=="--":
                    moves.append(Move((r,c),(r-2,c),self.board))                    
            if c-1>=0:
                if self.board[r-1][c-1][0]=='b':
                    moves.append(Move((r,c),(r-1,c-1),self.board))
            if c+1<=7:
                if self.board[r-1][c+1][0]=='b':
                    moves.append(Move((r,c),(r-1,c+1),self.board))
        else:
            if self.board[r+1][c]=="--":
                moves.append(Move((r,c),(r+1,c),self.board))
                if r==1 and self.board[r+2][c]=="--":
                    moves.append(Move((r,c),(r+2,c),self.board))
            if c-1>=0:
                if self.board[r+1][c-1][0]=='w':
                    moves.append(Move((r,c),(r+1,c-1),self.board))
            if c+1<=7:
                if self.board[r+1][c+1][0]=='w':
                    moves.append(Move((r,c),(r+1,c+1),self.board))
                    
                    
    def getRookMoves(self,r,c,moves):
        direction=((-1,0),(0,-1),(1,0),(0,1))
        enemyColor="b" if self.whiteToMove else "w"   
        for d in direction:
            for i in range(1,8):
                endRow=r+d[0]*i
                endCol=c+d[1]*i
                if 0<=endRow<8 and 0<=endCol<8:
                    endPiece =self.board[endRow][endCol]
                    if endPiece=="--":
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0]==enemyColor:
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else:
                        break
                else:
                    break
                
    def getBishopMoves(self,r,c,moves):
        direction=((-1,-1),(1,-1),(1,1),(-1,1))
        enemyColor="b" if self.whiteToMove else "w"   
        for d in direction:
            for i in range(1,8):
                endRow=r+d[0]*i
                endCol=c+d[1]*i
                if 0<=endRow<8 and 0<=endCol<8:
                    endPiece =self.board[endRow][endCol]
                    if endPiece=="--":
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0]==enemyColor:
                        moves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else:
                        break
                else:
                    break
                
    def getQueenMoves(self,r,c,moves):
        self.getBishopMoves(r,c,moves)
        self.getRookMoves(r,c,moves)
        
                   
    
    def getKnightMoves(self,r,c,moves):
        knightmoves =((2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
        allyColor ='w' if self.whiteToMove else 'b'
        for n in knightmoves:
            endRow=r+n[0]
            endCol=c+n[1]
            if 0<=endRow<8 and 0<=endCol<8:
                    endPiece =self.board[endRow][endCol]
                    if endPiece[0] != allyColor:
                        moves.append(Move((r,c),(endRow,endCol),self.board))
    
    def getKingMoves(self,r,c,moves):
        kingmoves =((-1,0),(0,-1),(1,0),(0,1),(-1,-1),(1,-1),(1,1),(-1,1))
        allyColor ='w' if self.whiteToMove else 'b'
        for k in kingmoves:
            endRow=r+k[0]
            endCol=c+k[1]
            if 0<=endRow<8 and 0<=endCol<8:
                    endPiece =self.board[endRow][endCol]
                    if endPiece[0]!=allyColor:
                        moves.append(Move((r,c),(endRow,endCol),self.board))

            
                       
                
                
                
                
class Move():
    
    
    ranksToRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = {v:k for k, v in ranksToRows.items()}
    filesToCols = {"h":7, "g":6, "f":5, "e":4, "d":3, "c":2, "b":1, "a":0}
    colsToFiles = {v:k for k, v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, board1):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol= endSq[1]
        self.pieceMoved = board1[self.startRow][self.startCol]
        self.pieceCaptured = board1[self.endRow][self.endCol]
        self.moveID = self.startRow*1000 +self.startCol*100 +self.endRow*10 +self.endCol    
    
    
    def __eq__(self,other):
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False    
            
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        
    def getRankFile(self,r,c):
        return self.colsToFiles[c]+ self.rowsToRanks[r]
    
        