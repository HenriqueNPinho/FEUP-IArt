from pieces import *
from queue import Queue
from state import *
import numpy as np


board_size = 6
board = [[' ']*board_size for _ in range(board_size)]

def get_human_move(pos):
    move='N'
    while move not in pos:
        print("available moves: ")
        print(pos)
        move=input("Select ur move: ")
    return move
    

def human(initial_state):
    states = Queue()
    states.put(initial_state)
    current_state = initial_state

    while current_state.pos != (len(board)-1, 0):

        valid_pos=[]
        for d in ['L', 'R', 'U', 'D']:
            new_state = move(current_state, d)
            if valid_state(new_state):
                valid_pos.append(new_state.dir)

        draw_board(current_state)

        dir = get_human_move(valid_pos)

        current_state = move(current_state, dir)


def main():

    rook = Rook((2, 4), board_size)
    bishop = Bishop((4, 1), board_size)
    king = King((3, 4), board_size)
    queen = Queen((1, 1), board_size)
    knight = Knight((2, 4), board_size)

    pieces = [bishop,queen,king]
    
    for piece in pieces:
        print(piece, piece.moves)

    print()

    remove_pieces_moves(pieces, board_size)

    for piece in pieces:
        print(piece, piece.moves)

    initial_pos = (0, board_size - 1)

    initial_state = State(initial_pos, board, pieces)

    aux = input("1 for Human, 0 for PC: ")

    
    if aux == '0':
        draw_board(initial_state)
        print()
        bfs_state(initial_state)
    else: 
        human(initial_state)


def move(state, dir):
    current_pos = state.pos
    if dir == 'U':
        next_pos = (current_pos[0], current_pos[1] - 1)
    elif dir == 'D':
        next_pos = (current_pos[0], current_pos[1] + 1)
    elif dir == 'L':
        next_pos = (current_pos[0] - 1, current_pos[1])
    elif dir == 'R':
        next_pos = (current_pos[0] + 1, current_pos[1])

    return State(next_pos, state.board, state.pieces, dir, state, state.depth + 1)


def draw_board(state):
    board = state.board
    pieces = state.pieces
    path = state.get_path()
    board_size = len(board)

    pos = []

    for p in path:
        (a,b,_) = p
        pos.append((a,b))

    print('___'*board_size)
    for x, row in enumerate(board):
        print('|',end='')
        for y, col in enumerate(row):
            if (y,x) in pos:
                print('+ ', end='')
            else:
                for piece in pieces:
                    if piece.pos == (y,x):
                        col = piece.symbol
                print(col + ' ', end='')
            print('|',end='')
        print()
        print('---'*board_size)


def bfs_state(initial_state):
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    
    while not end_state(current_state):
        current_state = states.get()
        for d in ['L', 'R', 'U', 'D']:
            new_state = move(current_state, d)
            if valid_state(new_state):
                states.put(new_state)

    draw_board(current_state)

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


def is_valid(path):
    (x,y,d) = path[-1]

    for i in range(0, len(path)-1):
        (a,b,_) = path[i]

        if (x,y) == (a,b):
            return False
        if d == 'R':
            if (a, b) in [(x, y+1), (x, y-1), (x+1, y), (x+1, y-1), (x+1, y+1)]:
                return False
        elif d == 'L':
            if (a, b) in [(x, y-1), (x, y+1), (x-1, y), (x-1, y-1), (x-1, y+1)]:
                return False
        elif d == 'U':
            if (a, b) in [(x+1, y), (x-1, y), (x, y-1), (x+1, y-1), (x-1, y-1)]:
                return False
        elif d == 'D':
            if (a, b) in [(x+1, y), (x-1, y), (x-1, y+1), (x+1, y+1), (x, y+1)]:
                return False
    return True

def end_state(state):
    final_pos = (len(state.board) - 1, 0)

    if state.pos != final_pos:
        return False

    if not equal_final_hits(state):
        return False

    return True

def equal_final_hits(state):
    hits = state.get_pieces_hits()
    return all(hit == hits[0] for hit in hits)


if __name__ == "__main__":
    main()

