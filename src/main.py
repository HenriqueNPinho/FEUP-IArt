from threading import currentThread
from pieces import *
from queue import PriorityQueue, Queue
from state import *
import numpy as np
from file import *
import human
from board import draw_board
import sys
from time import time

def main():
    if len(sys.argv) < 2:
        print('USAGE > python3 main.py <lvl>')
        return
        
    (board_size, pieces) = get_level(sys.argv[1])
    board = [[' ']*board_size for _ in range(board_size)]

    remove_pieces_moves(pieces, board_size)

    initial_pos = (0, board_size - 1)

    initial_state = State(initial_pos, board, pieces)

    aux = input("1 for Human, 0 for PC: ")

    
    if aux == '0':
        draw_board(initial_state)
        print()
        #dfs(initial_state)
        #bfs(initial_state)
        a_star(initial_state)
    else: 
        human.human(initial_state)


def get_new_state(state, dir):
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


def bfs(current_state):
    states = Queue()
    states.put(current_state)
    state_expanded = False
    states_expanded = 0
    max_states = 0
    
    bfs_start = time()
    while not end_state(current_state):
        current_state = states.get()
        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                max_states += 1
                state_expanded = True
                states.put(new_state)
        if state_expanded:
            states_expanded += 1
            state_expanded = False
    bfs_end = time()
    
    draw_board(current_state)
    print(f'BFS Time: {bfs_end - bfs_start} s')
    print(f'Nodes expanded: {states_expanded}')
    print(f'Max Memory: {max_states*sys.getsizeof(current_state)/1000} KB')
    print('States: ', states.qsize(), 'Depth: ', current_state.depth, 'Solution: ',current_state.get_path(), sep='\n')
    return current_state

def bfs_test(current_state):
    states = Queue()
    states.put(current_state)
    bfs_start = time()
    i=0
    while True:
        if end_state(current_state):
            print('end')
            i +=1
            if i > 1:
                break
        current_state = states.get()
        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                states.put(new_state)
    bfs_end = time()
    
    draw_board(current_state)
    print(f'BFS Time: {bfs_end - bfs_start}')
    print('States: ', states.qsize(), 'Depth: ', current_state.depth, 'Solution: ',current_state.get_path(), sep='\n')
    return current_state

def dfs(current_state):
    states = [current_state]
    state_expanded = False
    states_expanded = 0
    max_states = 0

    dfs_start = time()
    while not end_state(current_state):
        current_state = states.pop()
        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                states.append(new_state)
                max_states += 1
                state_expanded = True
        if state_expanded:
            states_expanded += 1
            state_expanded = False
    dfs_end = time()
    
    draw_board(current_state)
    print(f'DFS Time: {dfs_end - dfs_start} s')
    print(f'Nodes expanded: {states_expanded}')
    print(f'Max Memory: {max_states*sys.getsizeof(current_state)/1000} KB')
    print('Solution: ', current_state.get_path(), sep='\n')
    return current_state

def a_star(current_state):
    visited_states = set()
    states = PriorityQueue()
    states.put(current_state)
    
    a_star_start = time()
    while not end_state(current_state):
        current_state = states.get()
        
        if current_state in visited_states:
            continue

        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                states.put(new_state)

        visited_states.add(current_state)

    a_star_end = time()
    print(f'Time: {a_star_end-a_star_start}')
    draw_board(current_state)

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

    return equal_final_hits(state)
       

def equal_final_hits(state):
    hits = state.get_pieces_hits()
    return all(hit == hits[0] for hit in hits)


if __name__ == "__main__":
    main()