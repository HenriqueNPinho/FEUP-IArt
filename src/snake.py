class Snake:
    def __init__(self, board_size):
        self.pos = (0, board_size-1)
        self.s = 'S'


    def up(self):
        self.pos = (self.pos[0], self.pos[1]-1)
        self.s = '|'

    def down(self):
        self.pos = (self.pos[0], self.pos[1]+1)
        self.s = '|'

    def right(self):
        self.pos = (self.pos[0]+1, self.pos[1])
        self.s = '-'

    def left(self):
        self.pos = (self.pos[0]-1, self.pos[1])
        self.s = '-'

    