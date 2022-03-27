class State:
    def __init__(self, snake, board, pieces):
        self.snake = snake
        self.board = board
        self.pieces = pieces


    def up(self, snake, board):
        snake.up()
        snake.draw()

    def print(self, board, pieces, snake):
        x = 0
        y = 0
        for row in board:
            print('|', end='')
            for col in row:
                for piece in pieces:
                    if piece.pos == (x,y):                        
                        col = piece.p
                if snake.pos == (x, y):
                    col = snake.s
                print(col + ' |', end='')
                x = x+1
            x = 0
            y = y+1
            print('\n' + '-'*16)