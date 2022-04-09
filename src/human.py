from queue import Queue
from main import get_new_state, valid_state, draw_board

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
    board = initial_state.board

    while current_state.pos != (len(board)-1, 0):

        valid_pos=[]
        for d in ['L', 'R', 'U', 'D']:
            new_state = get_new_state(current_state, d)
            if valid_state(new_state):
                valid_pos.append(new_state.dir)

        draw_board(current_state)

        dir = get_human_move(valid_pos)

        current_state = get_new_state(current_state, dir)