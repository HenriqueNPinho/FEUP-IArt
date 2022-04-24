import queue
from time import time
from board import draw_board
from operators import *


def dfs(current_state):
    visited_states = set()
    states = [current_state]
    state_expanded = False
    states_expanded = 0
    max_states = 0

    while not end_state(current_state):
        current_state = states.pop()

        if current_state in visited_states:
            continue

        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                if new_state in visited_states:
                    continue
                states.append(new_state)
                max_states += 1
                state_expanded = True
        if state_expanded:
            states_expanded += 1
            state_expanded = False
        
        visited_states.add(current_state)
    
    return (current_state, max_states, states_expanded)


def a_star(current_state):
    visited_states = set()
    states = queue.PriorityQueue()
    states.put(current_state)
    state_expanded = False
    states_expanded = 0
    max_states = 0
    
    while not end_state(current_state):
        current_state = states.get()
        
        if current_state in visited_states:
            continue

        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                if new_state in visited_states:
                    continue
                max_states += 1
                state_expanded = True
                states.put(new_state)
            
            if state_expanded:
                states_expanded += 1
                state_expanded = False

        visited_states.add(current_state)

    return (current_state, max_states, states_expanded)


def bfs(current_state):
    visited_states = set()
    states = queue.Queue()
    states.put(current_state)
    state_expanded = False
    states_expanded = 0
    max_states = 0
    
    while not end_state(current_state):
        current_state = states.get()

        if current_state in visited_states:
            continue

        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                if new_state in visited_states:
                    continue
                max_states += 1
                state_expanded = True
                states.put(new_state)
                
        if state_expanded:
            states_expanded += 1
            state_expanded = False

        visited_states.add(current_state)
    
    return (current_state, max_states, states_expanded)





# --- Para APAGAR (usado para testar puzzles) -----
def a_star_test(current_state):
    visited_states = set()
    states = queue.PriorityQueue()
    states.put(current_state)
    state_expanded = False
    states_expanded = 0
    max_states = 0
    
    while True:
        if end_state(current_state):
            print('end')
            break
        current_state = states.get()
        
        if current_state in visited_states:
            continue

        for dir in 'LRUD':
            new_state = get_new_state(current_state, dir)
            if valid_state(new_state):
                if new_state in visited_states:
                    continue
                max_states += 1
                state_expanded = True
                states.put(new_state)
            
            if state_expanded:
                states_expanded += 1
                state_expanded = False

        visited_states.add(current_state)

    return (current_state, max_states, states_expanded)
