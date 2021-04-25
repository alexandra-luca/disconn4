import numpy as np
from PIL import Image

#Variable
WIDTH = 7
HEIGHT = 6
TURN = 1
GAMEOVER = False
BOARD = np.zeros((HEIGHT,WIDTH))

class Render:
    player1_path = 'player1.png'
    player2_path = 'player2.png'
    board_path = 'bg.png'

    def __init__(self):
        self.player1_image = Image.open(Render.player1_path)
        self.player2_image = Image.open(Render.player2_path)
        self.board_image = Image.open(Render.board_path)

    def __line_pixel_transform(self, line):
        return line * 100 + 15

    def __coll_pixel_transform(self, coll):
        return coll * 100 + 10

    def render_matrix(self, matrix):
        '''
        Param matrix: a matrix represnting the current board configuration
        Return value: returns a rendering of the board
        '''
        bg = self.board_image.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue

                position = (
                    self.__line_pixel_transform(j),
                    self.__coll_pixel_transform(i)
                )

                if matrix[i][j] == 1:
                    bg.paste(self.player1_image.copy(), position, self.player1_image)
                elif matrix[i][j] == 2:
                    bg.paste(self.player2_image.copy(), position, self.player2_image)
        return bg

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
                return True
    #Vertical
    for i in range(WIDTH):
        for j in range(HEIGHT - 3):
            if BOARD[j][i] == player and BOARD[j+1][i] == player and BOARD[j+2][i] and BOARD[j+3][i] == player:
                return True
    #Diagonal +
    for i in range(WIDTH - 3):
        for j in range(HEIGHT - 3):
            if BOARD[j][i] == player and BOARD[j+1][i+1] == player and BOARD[j+2][i+1] and BOARD[j+3][i+1] == player:
                return True
    #Diagonal -
    for i in range(WIDTH - 3):
        for j in range(3,HEIGHT):
            if BOARD[j][i] == player and BOARD[j-1][i+1] == player and BOARD[j-2][i+1] and BOARD[j-3][i+1] == player:
                return True
    return 0

def game(BOARD,GAMEOVER,TURN):
    while GAMEOVER == False: 
        if TURN == 1:
            #Commands range (0-6)
            col = int(input("Player1:"))
            if BOARD[HEIGHT-1][col] == 0:
                insert_jeton(BOARD,empty_row(BOARD,col),col,1)
                GAMEOVER =  win(BOARD,1)
                if GAMEOVER:
                    winner = (r.render_matrix(np.flip(BOARD,0)),TURN)
                    return winner
            TURN += 1
            r = Render()
            r.render_matrix(np.flip(BOARD,0)).show()
        else:
            col = int(input("Player2:"))
            if BOARD[HEIGHT-1][col] == 0:
                insert_jeton(BOARD,empty_row(BOARD,col),col,2)
                GAMEOVER =  win(BOARD,2)
                if GAMEOVER:
                    winner = (r.render_matrix(np.flip(BOARD,0)),TURN)
                    return winner
            TURN -= 1 
        
            r = Render()
            r.render_matrix(np.flip(BOARD,0)).show()
pass

if __name__ == "__main__":
    '''
    Driver code to illustrate the functionality
    '''
    #congrats[0] image with last move
    #congrats[1] number of player
    congrats = game(BOARD,GAMEOVER,TURN)