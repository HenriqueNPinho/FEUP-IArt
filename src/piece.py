class Piece:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves

    def set_moves(self, i):
        pass




class Rook(Piece):
    def __init__(self, pos, moves=[]):
        super().__init__(pos, moves)
    
    def set_moves(self, i):
        self.moves.append((self.pos[0], self.pos[1]+i))
        self.moves.append((self.pos[0], self.pos[1]-i))
        self.moves.append((self.pos[0]+i, self.pos[1]))
        self.moves.append((self.pos[0]-i, self.pos[1]))





class Bishop(Piece):
    def __init__(self, pos, moves=[]):
        super().__init__(pos, moves)

    def set_moves(self, i):
        self.moves.append((self.pos[0]+i, self.pos[1]+i))
        self.moves.append((self.pos[0]-i, self.pos[1]-i))
        self.moves.append((self.pos[0]+i, self.pos[1]-i))
        self.moves.append((self.pos[0]-i, self.pos[1]+i))





class King(Piece):
    def __init__(self, pos, moves=[]):
        super().__init__(pos, moves)

    def set_moves(self):
        
        up = self.pos[1]-1
        down = self.pos[1]+1
        right = self.pos[0]+1
        left = self.pos[0]-1
        self.moves.append((self.pos[0], up))
        self.moves.append((right, down))
        self.moves.append((right, self.pos[1]))
        self.moves.append((right, down))
        self.moves.append((left, self.pos[1]))
        self.moves.append((left, down))
        self.moves.append((left, up))





class Queen(Piece):
    def __init__(self, pos, moves=[]):
        super().__init__(pos, moves)

    def set_moves(self, i):
        self.moves.append((self.pos[0], self.pos[1]+i))
        self.moves.append((self.pos[0], self.pos[1]-i))
        self.moves.append((self.pos[0]+i, self.pos[1]+i))
        self.moves.append((self.pos[0]+i, self.pos[1]))
        self.moves.append((self.pos[0]+i, self.pos[1]-i))
        self.moves.append((self.pos[0]-i, self.pos[1]))
        self.moves.append((self.pos[0]-i, self.pos[1]+i))
        self.moves.append((self.pos[0]-i, self.pos[1]-i))




class Knight(Piece):
    def __init__(self, pos, moves=[]):
        super().__init__(pos, moves)

    def set_moves(self):
        self.moves.append((self.pos[0]+2, self.pos[1]-1))
        self.moves.append((self.pos[0]+1, self.pos[1]-2))
        self.moves.append((self.pos[0]-1, self.pos[1]-2))
        self.moves.append((self.pos[0]-2, self.pos[1]-1))
        self.moves.append((self.pos[0]-2, self.pos[1]+1))
        self.moves.append((self.pos[0]-1, self.pos[1]+2))
        self.moves.append((self.pos[0]+1, self.pos[1]+2))
        self.moves.append((self.pos[0]+2, self.pos[1]+1))
        
