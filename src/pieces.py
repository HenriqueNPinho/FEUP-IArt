import pygame

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
    
    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/rook.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)


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

    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/bishop.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)




class King:
    def __init__(self, pos, moves=[]):
        self.pos = pos
        self.moves = moves
        self.symbol = 'K'
        self.score = 0

    def set_moves(self):
        (x, y) = self.pos
        
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

    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/king.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)



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

    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/queen.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)


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
    
    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/knight.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)
