import enum
from pieces import *
from draw import draw_big_board, draw_small_board
import pygame
from queue import Queue
import numpy as np
import pygame_menu 

board_size = 5

board = [[' ']*board_size for _ in range(board_size)]

def print_board(board, pieces):
        x = 0
        y = 0
        for row in board:
            print('|', end='')
            for col in row:
                for piece in pieces:
                    if piece.pos is (x,y):                        
                        col = piece.symbol
                
                print(col + ' |', end='')
                x = x+1
            x = 0
            y = y+1
            print('\n' + '-'*16)

def draw_board(board, moves=""):
    x = 0
    y = len(board)-1
    pos = set()
    pos.add((x,y))
    for move in moves:
        if move == 'U':
            y-=1
        if move == 'D':
            y+=1
        if move == 'R':
            x+=1
        if move == 'L':
            x-=1
        pos.add((x,y))

    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if (y,x) in pos:
                print('+ ', end='')
            else:
                print(col + ' ', end='')
        print()


def set_pieces_moves(board, pieces):
    for piece in pieces:
        if type(piece).__name__ != 'King' and type(piece).__name__ != 'Knight':
            for i in range(1, board_size):
                piece.set_moves(i)
        else:
            piece.set_moves()
        remove_unnecessary_moves(piece)

    for i in range(len(pieces)):
        for j in range(i+1, len(pieces)):
            for move in list(pieces[i].moves):
                if move == pieces[j].pos:
                    pieces[i].moves.remove(move)
            remove_more_moves(board, pieces[i],pieces[j].pos)    


def remove_unnecessary_moves(piece):
    for move in list(piece.moves):
        if move[0] < 0 or move[1] < 0:
            piece.moves.remove(move)
            continue
        if move[0] > board_size-1 or move[1] > board_size-1:
            piece.moves.remove(move)



def same_score(pieces):
    scores = []
    for piece in pieces:
        scores.append(piece.score)
    return all(score == scores[0] for score in scores)


def valid(board, pieces, moves):
    x = 0
    y = len(board)-1

    path = [(x,y,'S')]

    for move in moves:
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1

        path.append((x,y,move))

        if not(0 <= x < len(board) and 0 <= y < len(board)):
            return False

        for piece in pieces:
            if (x,y) == piece.pos:
                return False   

    for i in range(0, len(path)):
        for j in range(0, i):
            if i == j:
                continue
            (x,y,d) = path[i]
            (w,z,_) = path[j]
            if (x,y) == (w,z):
                return False
            if d == 'R':
                if (x,y+1) == (w,z):
                    return False
                if (x,y-1) == (w,z):
                    return False
                if (x+1,y) == (w,z):
                    return False
                if (x+1,y-1) == (w,z):
                    return False
                if (x+1,y+1) == (w,z):
                    return False
            elif d == 'L':
                if (x,y-1) == (w,z):
                    return False
                if (x,y+1) == (w,z):
                    return False
                if (x-1,y) == (w,z):
                    return False
                if (x-1,y-1) == (w,z):
                    return False
                if (x-1,y+1) == (w,z):
                    return False
            elif d == 'U':
                if (x+1,y) == (w,z):
                    return False
                if (x-1,y) == (w,z):
                    return False
                if (x,y-1) == (w,z):
                    return False
                if (x+1,y-1) == (w,z):
                    return False
                if (x-1,y-1) == (w,z):
                    return False
            elif d == 'D':
                if (x+1,y) == (w,z):
                    return False
                if (x-1,y) == (w,z):
                    return False
                if (x-1,y+1) == (w,z):
                    return False
                if (x+1,y+1) == (w,z):
                    return False
                if (x,y+1) == (w,z):
                    return False
            
    return True


def p(path):
    moves = list(path.keys())
    for pos in path:
        d = path[pos]
        if d == 'U':
            for move in moves:
                if (pos[0]+1,pos[1]) == move:
                    return False
                elif (pos[0]-1,pos[1]) == move:
                    return False
                elif(pos[0], pos[1]-1) == move:
                    return False
                elif(pos[0]-1, pos[1]-1) == move:
                    return False
                elif(pos[0]+1,pos[1]-1) == move:
                    return False
        elif d == 'D':
            for move in moves:
                if (pos[0]-1,pos[1]) == move:
                    return False
                elif (pos[0]+1,pos[1]) == move:
                    return False
                elif(pos[0], pos[1]+1) == move:
                    return False
                elif(pos[0]+1, pos[1]+1) == move:
                    return False
                elif(pos[0]-1,pos[1]+1) == move:
                    return False
        elif d == 'L':
            for move in moves:
                if (pos[0],pos[1]-1) == move:
                    return False
                elif (pos[0],pos[1]+1) == move:
                    return False
                elif(pos[0]-1, pos[1]-1) == move:
                    return False
                elif(pos[0]-1, pos[1]) == move:
                    return False
                elif(pos[0]-1,pos[1]+1) == move:
                    return False
        elif d == 'R':
            for move in moves:
                if (pos[0],pos[1]+1) == move:
                    return False
                elif (pos[0],pos[1]-1) == move:
                    return False
                elif(pos[0]+1, pos[1]-1) == move:
                    return False
                elif(pos[0]+1, pos[1]) == move:
                    return False
                elif(pos[0]+1,pos[1]+1) == move:
                    return False

    return True


        

def remove_more_moves(board, piece, pos):
    (x,y) = tuple(np.subtract(piece.pos,pos))

    if x == 0 and y < 0:
        for i in range(pos[1]+1,len(board)):
            for move in list(piece.moves):
                if move == (pos[0],i):
                    piece.moves.remove(move)


def bfs(board, pieces):
    moves = Queue()
    moves.put("")
    add = ""

    while not end(board, pieces, add): 
        add = moves.get()
        #print(add)
        for d in ['L', 'R', 'U', 'D']:
            move = add + d
            if valid(board, pieces, move):
                moves.put(move)

def count_score(x,y,pieces):
    for piece in pieces:
            for piece_move in piece.moves:
                    if (x,y) == piece_move:
                        piece.score +=1

def end(board, pieces, moves):
    x = 0
    y = len(board) - 1
    path = {(x,y):'S'}
    count_score(x,y,pieces)
    for move in moves:
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1
        path[(x,y)] = move
        count_score(x,y,pieces)       

    #if not p(path): 
     #   path.clear()
      #  return False


    if ((x,y) == (len(board)-1,0) and same_score(pieces)):
        print('Solution:', moves)
        draw_board(board, moves)
        return True
        
    reset_score(pieces)
    return False

def reset_score(pieces):
    for piece in pieces:
        piece.score = 0

def read_file(file):
    f = open(file, 'r')
    board = f.readlines()
    return board

def main():
    #print_board(board)
    rook = Rook((4, 3))
    bishop = Bishop((2, 4))
    king = King((1,3))
    queen = Queen((1,1))
    knight = Knight((3,4))

    pieces = [bishop,rook]

    set_pieces_moves(board, pieces)

    print_board(board, pieces)


    bfs(board, pieces)

    

if __name__ == "__main__":
    main()

