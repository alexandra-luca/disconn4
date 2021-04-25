import numpy as np

#Variable
WIDTH = 7
HEIGHT = 6
TURN = 1
GAMEOVER = 0
BOARD = np.zeros((HEIGHT,WIDTH))

#Functions
def empty_row(BOARD,col):
    for i in range(HEIGHT):
        if BOARD[i][col] == 0:
            return i

def insert_jeton(BOARD,row,col,player):
    BOARD[row][col] = player

def win(BOARD,player):
    #Horizontal
    for i in range(WIDTH - 3):
        for j in range(HEIGHT):
            if BOARD[j][i] == player and BOARD[j][i+1] == player and BOARD[j][i+2] and BOARD[j][i+3] == player:
                return 1
    #Vertical
    for i in range(WIDTH):
        for j in range(HEIGHT - 3):
            if BOARD[j][i] == player and BOARD[j+1][i] == player and BOARD[j+2][i] and BOARD[j+3][i] == player:
                return 1
    #Diagonal +
    for i in range(WIDTH - 3):
        for j in range(HEIGHT - 3):
            if BOARD[j][i] == player and BOARD[j+1][i+1] == player and BOARD[j+2][i+1] and BOARD[j+3][i+1] == player:
                return 1
    #Diagonal -
    for i in range(WIDTH - 3):
        for j in range(3,HEIGHT):
            if BOARD[j][i] == player and BOARD[j-1][i+1] == player and BOARD[j-2][i+1] and BOARD[j-3][i+1] == player:
                return 1
    return 0

#Loop
while GAMEOVER == 0: 
    if TURN == 1:
        col = int(input("Player1:"))
        if BOARD[HEIGHT-1][col] == 0:
            insert_jeton(BOARD,empty_row(BOARD,col),col,1)
            GAMEOVER =  win(BOARD,1)
        TURN += 1
    else:
        col = int(input("Player2:"))
        if BOARD[HEIGHT-1][col] == 0:
            insert_jeton(BOARD,empty_row(BOARD,col),col,2)
            GAMEOVER =  win(BOARD,2)
        TURN -= 1
    print(np.flip(BOARD, 0)) 
