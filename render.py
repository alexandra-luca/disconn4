from PIL import Image

class Render:
    player1_path = 'res/player1.png'
    player2_path = 'res/player2.png'
    winner1_path = 'res/winner1.png'
    winner2_path = 'res/winner2.png'
    draw_path = 'res/draw.png'
    board_path = 'res/bg.png'
        
    def __init__(self):
        self.player1_image = Image.open(Render.player1_path)
        self.player2_image = Image.open(Render.player2_path)
        self.winner1_image = Image.open(Render.winner1_path)
        self.winner2_image = Image.open(Render.winner2_path)
        self.draw_image = Image.open(Render.draw_path)
        self.board_image = Image.open(Render.board_path)
    
    def __line_pixel_transform(self, line):
        return line * 100 + 14

    def __coll_pixel_transform(self, coll):
        return coll * 100 + 61

    def render_matrix(self, matrix, winner = 0):
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
        
        if winner == 1:
            bg.paste(self.winner1_image.copy(), (0, 0), self.winner1_image)
        elif winner == 2:
            bg.paste(self.winner2_image.copy(), (0, 0), self.winner2_image)
        elif winner == -1:
            bg.paste(self.draw_image.copy(), (0, 0), self.draw_image)

        return bg

if __name__ == "__main__":
    '''
    Driver code to illustrate the functionality
    '''
    matrix = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 2, 1, 0, 2, 0, 0],
        [0, 1, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 1, 1, 0],
        [0, 2, 2, 1, 1, 2, 1]
    ]
    r = Render()
    r.render_matrix(matrix).show()
    r.render_matrix(matrix, 1).show()
    r.render_matrix(matrix, 2).show()
    r.render_matrix(matrix, -1).show()
