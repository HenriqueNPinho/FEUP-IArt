from queue import Queue
from time import time
from board import draw_board
from operators import *
import search

keys = {
    'w':'U',
    'a':'L',
    's':'D',
    'd':'R'
}

def human(initial_state):
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    (objective_state,_,_) = search.a_star(initial_state)
    board = initial_state.board
    n_moves = 0
    won = True
    hint = 0
    print('\nUse WASD to move the snake!\n')
    
    start = time()
    while current_state.get_path() != objective_state.get_path():
        valid_pos = []
        
        if current_state.pos == (len(board)-1, 0):
            draw_board(current_state)
            print('\nYou Lose\n')
            print("Solution: ", objective_state.pieces_hits)
            print("Your play: ", current_state.pieces_hits)
            won = False
            break
        
        for d in ['L', 'R', 'U', 'D']:
            new_state = get_new_state(current_state, d)
            if valid_state(new_state):
                valid_pos.append(new_state.dir)
        
        draw_board(current_state)

        dir = get_human_move(valid_pos)

        if dir == 'B':
            if current_state.parent_node != None:
                current_state = current_state.parent_node
        elif dir == 'H':
            print('\nHint:')
            if hint == 0:
                print('Number of moves: ' + str(len(objective_state.get_path())-1))
                hint = 1
            elif hint == 1:
                print('Number of hits: ' + str(objective_state.get_pieces_hits()[0]))
                hint = 2
            else:
                print('Number of moves: ' + str(len(objective_state.get_path())-1))
                print('Number of hits: ' + str(objective_state.get_pieces_hits()[0]))
            n_moves -= 1
        else:
            current_state = get_new_state(current_state, dir)

        n_moves += 1
    end = time()

    if won:
        draw_board(current_state)
        score = get_score(end-start, n_moves, len(objective_state.board), objective_state.depth)

        print("\nYou Won\n")
        print(f'Number of moves: {n_moves}')
        print(f'Time spent: {end - start:.2f}')
        print(f'Score: {score:.2f}')


def get_human_move(pos):
    move=''

    while move.upper() not in pos:
        print("Available moves: ", pos)
        i = input("Select your move: ")
        
        if i == 'b':
            return i.upper()
        if i == 'h':
            return i.upper()
        else:
            move = keys.get(i, '')

    return move.upper()


def get_score(time, n_moves, board_size, max_moves):
    moves_score = max_moves/n_moves * 100
    time_score = 0
    if board_size < 7:
        if time < 10:
            time_score = 100
        else:
            time_score = 10/time * 100
    elif board_size > 7:
        if time < 20:
            time_score = 100
        else:
            time_score = 20/time * 100
    return (moves_score + time_score) / 2
