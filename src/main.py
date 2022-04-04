from typing import final
from pieces import *
from queue import Queue
import numpy as np
from state import *

board_size = 6

board = [[' ']*board_size for _ in range(board_size)]

def print_board(board, pieces):
        x = 0
        y = 0
        print('\n' + '-'*19)
        for row in board:
            print('|', end='')
            for col in row:
                for piece in pieces:
                    if piece.pos == (x,y): 
                                        
                        col = piece.symbol
                
                print(col + ' |', end='')
                x = x+1
            x = 0
            y = y+1
            print('\n' + '-'*19)

def draw_board(board, pieces, moves=""):
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
                for piece in pieces:
                    if piece.pos == (y,x):
                        col = piece.symbol
                print(col + ' ', end='')
        print()

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

    if not is_valid(path):
        return False
            
    return True

def is_valid(path):
    (x,y,d) = path[len(path)-1]
    for j in range(0, len(path)-1):
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

def bfs_state(initial_state):
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    
    while not end_state(current_state):
        current_state = states.get()
        for d in ['L', 'R', 'U', 'D']:
            new_state = current_state.move(d)
            if valid_state(new_state):
                states.put(new_state)
    
    print('States: ', states.qsize(), 'Depth: ', current_state.depth, 'Solution: ',current_state.get_path(), sep='\n')

def valid_state(state):
    (x, y) = state.pos
    board = state.board
    pieces = state.pieces

    if not(0 <= x < len(board) and 0 <= y < len(board)):
            return False

    for piece in pieces:
        if piece.pos == state.pos:
            return False

    return is_valid(state.get_path())
        


def count_score(x,y,pieces):
    for piece in pieces:
            for piece_move in piece.moves:
                    if (x,y) == piece_move:
                        piece.score +=1

def end_state(state):
    pieces = state.pieces

    final_pos = (len(state.board) - 1, 0)

    if state.pos != final_pos:
        return False

    if not check_final_hits(state):
        return False

    print()

    return True

def check_final_hits(state):
    hits = state.get_pieces_hits()
    return all(hit == hits[0] for hit in hits)



    
    


def end(board, pieces, moves):
    x = 0
    y = len(board) - 1
    
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
            
        count_score(x,y,pieces)       

    if ((x,y) == (len(board)-1,0) and same_score(pieces)):
        print('Solution:', moves)
        draw_board(board, pieces, moves)
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
    rook = Rook((5, 1), board_size)
    bishop = Bishop((2, 1), board_size)
    king = King((4,3), board_size)
    queen = Queen((2,0), board_size)
    knight = Knight((1,4), board_size)

    pieces = [queen,king,rook]

    initial_pos = (0, board_size - 1)

    initial_state = State(initial_pos,board, pieces)

   # for piece in pieces:
    #    print(piece.pos,piece.moves)

    a=input("1 for human, 0 for computer: ")

    #set_pieces_moves(board, pieces)

    print_board(board, pieces)
    if(a==0):
        #bfs(board, pieces)
        bfs_state(initial_state)
    else:
        print("fazer isto")


if __name__ == "__main__":
    main()

