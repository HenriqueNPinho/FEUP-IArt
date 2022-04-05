from queue import Queue
from main import *

def get_human_move(pos):
    print("available moves: ")
    print(pos)
    move=input("Select ur move: ")
    

def human(initial_state):
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    valid_pos=[]

    for d in ['L', 'R', 'U', 'D']:
        new_state = current_state.move(d)
        if valid_state(new_state):
            valid_pos.append(new_state.dir)
    print(valid_pos)
    ##states.put(new_state)
    #get_human_move(valid_pos)
    path = current_state.get_path()
    path_s = ''

    for pos in path:
        (x,y,d) = pos
        if d != 'S':
            path_s += d

    draw_board(board, current_state.pieces, path_s)