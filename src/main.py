from pieces import *
from queue import Queue
from state import *

board_size = 6
board = [[' ']*board_size for _ in range(board_size)]

def main():

    rook = Rook((5, 1), board_size)
    bishop = Bishop((2, 1), board_size)
    king = King((4,3), board_size)
    queen = Queen((2,0), board_size)
    knight = Knight((1,4), board_size)

    pieces = [queen,king,rook]

    initial_pos = (0, board_size - 1)

    initial_state = State(initial_pos,board, pieces)

    draw_board(board, pieces)

    bfs_state(initial_state)

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
    
    path = current_state.get_path()
    path_s = ''

    for pos in path:
        (x,y,d) = pos
        if d != 'S':
            path_s += d

    draw_board(board, current_state.pieces, path_s)

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


if __name__ == "__main__":
    main()

