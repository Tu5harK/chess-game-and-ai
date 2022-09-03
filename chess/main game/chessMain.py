import pygame as p
import chessEngine

WIDTH=HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES ={}

''' we are loading images w.r.t the piece name from the images folder into a IMAGES list'''


def loadImages():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    
    ''' just some basic functon of pygame to blit out the screen and set the screen color to white'''
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    
    '''loading our gamestate from the chessEngine'''
    gs = chessEngine.gamestate()
    
    '''getting valid moves'''
    validMoves =gs.getValidMoves() 
    moveMade = False
    
    ''' calling the loadImages'''
    loadImages()
    
    '''declaring sqselected tuple and playerclicks list with running bool'''
    running =True
    sqSelected = ()
    playerClicks =[]
    
    '''runnig the game loop'''
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN: 
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE 
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected =()
                    playerselect = []
                else:
                  sqSelected = (row,col)
                  playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = chessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        moveMade =True
                        gs.makeMove(move)
                        sqSelected= ()
                        playerClicks= [] 
                    else:
                        playerClicks =[sqSelected]
            
            elif e.type==p.KEYDOWN:
                if e.key==p.K_z:
                    gs.undoMove()
                    moveMade =True
        
        if moveMade:
            validMoves =gs.getValidMoves()  
            moveMade=False          
                                
        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen,gs)
        
def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)


def drawBoard(screen):
    colors = [p.Color("white"),p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color =colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
     
    
def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
              screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))




       
if __name__ == "__main__":
    main()
    

