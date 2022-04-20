import pygame
import numpy as np


class Rook:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'R'
        self.image = "../pieces/rook.png"
    
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



class Bishop:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'B'
        self.image = "../pieces/bishop.png"

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




class King:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'K'
        self.image = "../pieces/king.png"

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




class Queen:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'Q'
        self.image = "../pieces/queen.png"

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

class Knight:
    def __init__(self, pos, board_size=0):
        self.pos = pos
        self.moves = self.__set_moves(board_size)
        self.symbol = 'H'
        self.image = "../pieces/knight.png"

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
    




def remove_pieces_moves(pieces, board_size):
    for i in range(0, len(pieces)):
        piece = pieces[i]
        if type(piece).__name__ == 'King' or type(piece).__name__ == 'Knight':
            for j in range(0, len(pieces)):
                if i == j:
                    continue
                for move in piece.moves:
                    if move == pieces[j].pos:
                        pieces[i].moves.remove(move)
        else:
            remove_pieces_moves_aux(pieces, board_size)

def remove_pieces_moves_aux(pieces, board_size):
    
    for i in range(0, len(pieces)):
        piece = pieces[i]
        if not (type(piece).__name__ == 'King' or type(piece).__name__ == 'Knight'):
            for j in range(0, len(pieces)):
                if i == j:
                    continue
                else:
                    piece_2_pos = pieces[j].pos
                    (x, y) = tuple(np.subtract(piece.pos, piece_2_pos))
                    diff_x = abs(piece.pos[0] - piece_2_pos[0])
                    diff_y = abs(piece.pos[1] - piece_2_pos[1])

                    if x == 0 and y < 0: # DOWN
                        for k in range(piece_2_pos[1], board_size):
                            for move in piece.moves:
                                if move == (piece_2_pos[0], k):
                                    pieces[i].moves.remove(move)

                    if x == 0 and y > 0: # UP
                        for k in range(0, piece_2_pos[1]):
                            for move in piece.moves:
                                if move == (piece_2_pos[0], k):
                                    pieces[i].moves.remove(move)

                    if x < 0 and y == 0: # RIGHT
                        for k in range(piece_2_pos[0], board_size):
                            for move in piece.moves:
                                if move == (k, piece_2_pos[1]):
                                    pieces[i].moves.remove(move)

                    if x > 0 and y == 0: # LEFT
                        for k in range(0, piece_2_pos[0]+1):
                            for move in piece.moves:
                                if move == (k, piece_2_pos[1]):
                                    pieces[i].moves.remove(move)

                    if type(piece).__name__ == 'Bishop' or type(piece).__name__ == 'Queen':
                        if diff_x == diff_y:
                            if piece.pos[0] < piece_2_pos[0] and piece.pos[1] < piece_2_pos[1]:
                                for move in pieces[i].moves:
                                    for k in range(piece_2_pos[0], board_size):
                                        for l in range(piece_2_pos[1], board_size):
                                            if move == (k, l):
                                                pieces[i].moves.remove(move)

                            if piece.pos[0] < piece_2_pos[0] and piece.pos[1] > piece_2_pos[1]:
                                for move in pieces[i].moves:
                                    for k in range(piece_2_pos[0], board_size):
                                        for l in range(piece_2_pos[1], board_size):
                                            if move == (k, l):
                                                pieces[i].moves.remove(move)

                            if piece.pos[0] > piece_2_pos[0] and piece.pos[1] < piece_2_pos[1]:
                                for move in pieces[i].moves:
                                    for k in range(0, piece_2_pos[0]):
                                        for l in range(0, piece_2_pos[1]):
                                            if move == (k, l):
                                                pieces[i].moves.remove(move)

                            if piece.pos[0] > piece_2_pos[0] and piece.pos[1] > piece_2_pos[1]:
                                for move in pieces[i].moves:
                                    for k in range(0, piece_2_pos[0]):
                                        for l in range(0, piece_2_pos[1]):
                                            if move == (k, l):
                                                pieces[i].moves.remove(move)
                
