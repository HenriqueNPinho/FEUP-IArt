class Rook:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves
        self.symbol = 'R'
        self.score = 0
    
    def set_moves(self, i):
        self.moves.append((self.pos[0], self.pos[1]+i))
        self.moves.append((self.pos[0], self.pos[1]-i))
        self.moves.append((self.pos[0]+i, self.pos[1]))
        self.moves.append((self.pos[0]-i, self.pos[1]))





class Bishop:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves
        self.symbol = 'B'
        self.score = 0

    def set_moves(self, i):
        self.moves.append((self.pos[0]+i, self.pos[1]+i))
        self.moves.append((self.pos[0]-i, self.pos[1]-i))
        self.moves.append((self.pos[0]+i, self.pos[1]-i))
        self.moves.append((self.pos[0]-i, self.pos[1]+i))





class King:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves
        self.symbol = 'K'
        self.score = 0

    def set_moves(self):
        (x, y) = self.pos
        
        up = (x, y-1)
        down = (x, y+1)
        right = (x+1, y)
        left = (x-1, y)
        up_right = (x+1, y-1)
        up_left = (x-1, y-1)
        down_right = (x+1, y+1)
        down_left = (x-1, y+1)

        self.moves.append(up)
        self.moves.append(down)
        self.moves.append(left)
        self.moves.append(right)
        self.moves.append(up_right)
        self.moves.append(up_left)
        self.moves.append(down_right)
        self.moves.append(down_left)



class Queen:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves
        self.symbol = 'Q'
        self.score = 0

    def set_moves(self, i):
        self.moves.append((self.pos[0], self.pos[1]+i))
        self.moves.append((self.pos[0], self.pos[1]-i))
        self.moves.append((self.pos[0]+i, self.pos[1]+i))
        self.moves.append((self.pos[0]+i, self.pos[1]))
        self.moves.append((self.pos[0]+i, self.pos[1]-i))
        self.moves.append((self.pos[0]-i, self.pos[1]))
        self.moves.append((self.pos[0]-i, self.pos[1]+i))
        self.moves.append((self.pos[0]-i, self.pos[1]-i))




class Knight:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves
        self.symbol = 'C'
        self.score = 0

    def set_moves(self):
        self.moves.append((self.pos[0]+2, self.pos[1]-1))
        self.moves.append((self.pos[0]+1, self.pos[1]-2))
        self.moves.append((self.pos[0]-1, self.pos[1]-2))
        self.moves.append((self.pos[0]-2, self.pos[1]-1))
        self.moves.append((self.pos[0]-2, self.pos[1]+1))
        self.moves.append((self.pos[0]-1, self.pos[1]+2))
        self.moves.append((self.pos[0]+1, self.pos[1]+2))
        self.moves.append((self.pos[0]+2, self.pos[1]+1))
        
