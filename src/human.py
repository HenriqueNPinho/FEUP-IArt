from queue import Queue
from time import time
from board import draw_board
import main
from operators import *
import search

keys = {
    'w':'U',
    'a':'L',
    's':'D',
    'd':'R'
}

def get_human_move(pos):
    move=''

    while move.upper() not in pos:
        print("Available moves: ", pos)
        i = input("Select your move: ")
        
        if i == 'b':
            return i.upper()
        else:
            move = keys.get(i, '')

    return move.upper()
    

def human(initial_state):
    
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    objective_state = search.bfs(initial_state)
    board = initial_state.board
    n_moves = 0
    
    start = time()
    while current_state.get_path() != objective_state.get_path():
        valid_pos = []
        
        for d in ['L', 'R', 'U', 'D']:
            new_state = get_new_state(current_state, d)
            if valid_state(new_state):
                valid_pos.append(new_state.dir)
        
        draw_board(current_state)

        if current_state.pos == (len(board)-1, 0):
            print("Solution: ", objective_state.pieces_hits)
            print("Your play: ", current_state.pieces_hits)

        dir = get_human_move(valid_pos)

        if dir == 'B':
            if current_state.parent_node != None:
                current_state = current_state.parent_node
        else:
            current_state = get_new_state(current_state, dir)

        n_moves += 1
    end = time()

    draw_board(current_state)

    print("\nYou Won")
    print(f'Number of moves: {n_moves}')
    print(f'Time spent: {end - start}')

    main.menu(initial_state)