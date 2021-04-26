import numpy as np
import winner_render

#Variable
WIDTH = 7
HEIGHT = 6
TURN = 1
GAMEOVER = 0
class Logic:

    board = np.zeros((HEIGHT,WIDTH))

#Functions
    def empty_row(self,col):
        for i in range(HEIGHT):
            if self.board[i][col] == 0:
                return i

    def insert_jeton(self,row,col,player):
        self.board[row][col] = player

    def win(self,player):
        #Horizontal
        for i in range(WIDTH - 3):
            for j in range(HEIGHT):
                if self.board[j][i] == player and self.board[j][i+1] == player and self.board[j][i+2] and self.board[j][i+3] == player:
                    return 1
        #Vertical
        for i in range(WIDTH):
            for j in range(HEIGHT - 3):
                if self.board[j][i] == player and self.board[j+1][i] == player and self.board[j+2][i] and self.board[j+3][i] == player:
                    return 1
        #Diagonal +
        for i in range(WIDTH - 3):
            for j in range(HEIGHT - 3):
                if self.board[j][i] == player and self.board[j+1][i+1] == player and self.board[j+2][i+2] and self.board[j+3][i+3] == player:
                    return 1
        #Diagonal -
        for i in range(WIDTH - 3):
            for j in range(3,HEIGHT):
                if self.board[j][i] == player and self.board[j-1][i+1] == player and self.board[j-2][i+2] and self.board[j-3][i+3] == player:
                    return 1
        return 0

    def game(self,GAMEOVER,TURN):
        while GAMEOVER == False: 
            if TURN == 1:
                #Commands range (0-6)
                col = int(input("Player1:"))
                if self.board[HEIGHT-1][col] == 0:
                    self.insert_jeton(self.empty_row(col),col,1)
                    GAMEOVER =  self.win(1)
                    if GAMEOVER:
                        winner = (r.render_matrix(np.flip(self.board,0),TURN),TURN)
                        return winner
                TURN += 1

                r = winner_render.Render()
                r.render_matrix(np.flip(self.board,0)).show()
            else:
                col = int(input("Player2:"))
                if self.board[HEIGHT-1][col] == 0:
                    self.insert_jeton(self.empty_row(col),col,2)
                    GAMEOVER =  self.win(2)
                    if GAMEOVER:
                        winner = (r.render_matrix(np.flip(self.board,0),TURN))
                        return winner
                TURN -= 1 
            
                r = winner_render.Render()
                r.render_matrix(np.flip(self.board,0)).show()

if __name__ == "__main__":
    gamer = Logic()
    #congrats[0] image with winner
    #congrats[1] number of player
    congrats = gamer.game(GAMEOVER,TURN)