import time
import random
from pieces import *
import search
from state import *
from file import *
import human
from board import draw_board
import sys
import performance

def main():
    if len(sys.argv) == 2:
        (board_size, pieces) = get_level(sys.argv[1])
    if len(sys.argv) < 2:
        (board_size, pieces) = get_level(choose_puzzle())
        
    init(board_size, pieces)


def init(board_size, pieces):
    board = [[' ']*board_size for _ in range(board_size)]

    remove_pieces_moves(pieces, board_size)

    initial_pos = (0, board_size - 1)

    initial_state = State(initial_pos, board, pieces)

    menu(initial_state)


def choose_puzzle():
    while True:
        print('\n1 - Board 5x5')
        print('2 - Board 6x6')
        print('3 - Board 8x8')
        i = input('\n> ')

        if i == '1':
            n = random.randint(1,10)
            print(n)
            return 'lvl'+str(n)
        elif i == '2':
            n = random.randint(11,20)
            return 'lvl'+str(n)
        elif i == '3':
            n = random.randint(21,22)
            return 'lvl'+str(n)


def menu(initial_state):
    new_level = False
    while True:
        print('\n=========================')
        print('|                       |')
        print('|  CHESS SNAKE PUZZLES  |')
        print('|                       |')
        print('=========================')
        draw_board(initial_state)
        print('\n')
        print('1 - Player', '2 - CPU', '3 - Level', '4 - Performance Metrics', '0 - Exit', sep='\n')
        aux = input('\n> ')

        if aux == '4':
            bfs_start = time.time()
            (final_state, max_states_bfs, states_expanded_bfs)  = search.bfs(initial_state)
            bfs_end = time.time()
            (final_state, max_states_dfs, states_expanded_dfs)  = search.dfs(initial_state)
            dfs_end = time.time()
            (final_state, max_states_a_star, states_expanded_a_star) = search.a_star(initial_state)
            a_star_end = time.time()
            
            max_states = [max_states_bfs*sys.getsizeof(final_state)/1000, max_states_dfs*sys.getsizeof(final_state)/1000, max_states_a_star*sys.getsizeof(final_state)/1000]
            times = [bfs_end - bfs_start, dfs_end - bfs_end, a_star_end - dfs_end]
            states_expanded = [states_expanded_bfs, states_expanded_dfs, states_expanded_a_star]

            performance.draw_chart_time(len(initial_state.board), times)
            performance.draw_chart_max(len(initial_state.board), max_states)
            performance.draw_chart_expanded(len(initial_state.board), states_expanded)


        elif aux == '3':
            new_level = True
            break
        
        elif aux == '2':
            while True:
                print('\nSearch Methods:\n')
                print('1 - BFS (uninformed)', '2 - DFS (uninformed)', '3 - A* (informed)', sep='\n')
                i = input('\n> ')
                start = time.time()
                if i == '1':
                    (final_state, max_states, states_expanded)  = search.bfs(initial_state)
                elif i == '2':
                    (final_state, max_states, states_expanded)  = search.dfs(initial_state)
                elif i == '3':
                    (final_state, max_states, states_expanded) = search.a_star(initial_state)
                else:
                    break
                end = time.time()

                draw_board(final_state)
                print(f'Time: {end - start:.4f}s')
                print(f'Nodes expanded: {states_expanded}')
                print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB')
                print('Solution: ', final_state.get_path())

        elif aux == '1': 
            human.human(initial_state)
        elif aux == '0':
            return

    if new_level:
        (board_size, pieces) = get_level(choose_puzzle())
        init(board_size, pieces)


if __name__ == "__main__":
    main()