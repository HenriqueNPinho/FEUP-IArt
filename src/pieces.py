import pygame

class Rook:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'R'
        self.score = 0
    
    def __set_moves(self, board_size):
        moves = []
        for row in range(0, board_size):
            for col in range(0, board_size):
                for i in range(1, board_size):
                    if (row, col) == (self.pos[0] + i, self.pos[1]):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0], self.pos[1] + i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] - i, self.pos[1]):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0], self.pos[1] - i):
                        moves.append((row, col))
                        break
        return moves
    
    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/rook.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)


class Bishop:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'B'
        self.score = 0

    def __set_moves(self, board_size):
        moves = []
        for row in range(0, board_size):
            for col in range(0, board_size):
                for i in range(1, board_size):
                    if (row, col) == (self.pos[0] + i, self.pos[1] + i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] + i, self.pos[1] - i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] - i, self.pos[1] - i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] - i, self.pos[1] + i):
                        moves.append((row, col))
                        break
        return moves

    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/bishop.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)




class King:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'K'
        self.score = 0

    def __set_moves(self, board_size):
        moves = []
        for row in range(0, board_size):
            for col in range(0, board_size):
                if (row, col) == (self.pos[0] + 1, self.pos[1]):
                    moves.append((row, col))
                if (row, col) == (self.pos[0], self.pos[1] + 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 1, self.pos[1]):
                    moves.append((row, col))
                if (row, col) == (self.pos[0], self.pos[1] - 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] + 1, self.pos[1] + 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 1, self.pos[1] + 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 1, self.pos[1] - 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] + 1, self.pos[1] - 1):
                    moves.append((row, col))

        return moves

    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/king.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)



class Queen:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'Q'
        self.score = 0

    def __set_moves(self, board_size):
        moves = []
        for row in range(0, board_size):
            for col in range(0, board_size):
                for i in range(1, board_size):
                    if (row, col) == (self.pos[0] + i, self.pos[1]):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0], self.pos[1] + i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] - i, self.pos[1]):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0], self.pos[1] - i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] + i, self.pos[1] + i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] - i, self.pos[1] + i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] - i, self.pos[1] - i):
                        moves.append((row, col))
                        break
                    if (row, col) == (self.pos[0] + i, self.pos[1] - i):
                        moves.append((row, col))
                        break

        return moves

    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/queen.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)


class Knight:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'C'
        self.score = 0

    def __set_moves(self, board_size):
        moves = []
        for row in range(0, board_size):
            for col in range(0, board_size):
                if (row, col) == (self.pos[0] + 2, self.pos[1] - 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] + 1, self.pos[1] - 2):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 1, self.pos[1] - 2):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 2, self.pos[1] - 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 2, self.pos[1] + 1):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] - 1, self.pos[1] + 2):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] + 1, self.pos[1] + 2):
                    moves.append((row, col))
                if (row, col) == (self.pos[0] + 2, self.pos[1] + 1):
                    moves.append((row, col))

        return moves
    
    def draw(self,SCREEN, lvl):
         piece = pygame.image.load("pieces/knight.png")
         if lvl<=10:
             piece = pygame.transform.scale(piece, (144,144))
         else:
             piece = pygame.transform.scale(piece, (120,120))
         pygame.Surface.blit(SCREEN, piece, self.pos)
