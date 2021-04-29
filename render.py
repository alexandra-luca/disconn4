from PIL import Image

class Render:
    player1_path = 'res/player1.png'
    player2_path = 'res/player2.png'
    board_path = 'res/bg.png'
        
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

if __name__ == "__main__":
    '''
    Driver code to illustrate the functionality
    '''
    matrix = [
        [1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 2, 1]
    ]
    r = Render()
    r.render_matrix(matrix).show()
