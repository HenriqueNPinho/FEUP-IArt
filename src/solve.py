import sys
from time import time
import performance
from file import get_level
import main
import search


def solve_all_puzzles(difficulty, algo):
    if difficulty == '9':
        for i in range(1,23):
            (board_size, pieces) = get_level('lvl'+str(i))
            initial_state = main.init(board_size, pieces)
            times = []
            max = []
            states = []
            for j in range(1,4):
                start = time()
                if j == 1:
                    print('BFS')
                    (final_state, max_states, states_expanded)  = search.bfs(initial_state)
                elif j == 2:
                    print('DFS')
                    (final_state, max_states, states_expanded)  = search.dfs(initial_state)
                elif j == 3:
                    print('A*')
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                end = time()

                times.append(end-start)
                max.append(max_states*sys.getsizeof(final_state)/1000)
                states.append(states_expanded)

                print(f'Level {i}')
                print(f'Time: {end - start:.4f}s')
                print(f'Nodes expanded: {states_expanded}')
                print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')
            
            #performance.draw_chart_time(len(initial_state.board), times, i)
            #performance.draw_chart_max(len(initial_state.board), max, i)
            #performance.draw_chart_expanded(len(initial_state.board), states, i)
                
    if difficulty == '0':
        for i in range(1, 4):
            if i == 1:
                print('BFS\n')
            elif i == 2:
                print('DFS\n')
            elif i == 3:
                print('A*\n')
            for j in range(1, 23):
                (board_size, pieces) = get_level('lvl'+str(j))
                initial_state = main.init(board_size, pieces)
                start = time()
                if i == 1:
                    (final_state, max_states, states_expanded)  = search.bfs(initial_state)
                elif i == 2:
                    (final_state, max_states, states_expanded)  = search.dfs(initial_state)
                elif i == 3:
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                end = time()
 
                print(f'Level {j}')
                print(f'Time: {end - start:.4f}s')
                print(f'Nodes expanded: {states_expanded}')
                print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')

    if difficulty == '1':
        for i in range(1,11):
            (board_size, pieces) = get_level('lvl'+str(i))
            initial_state = main.init(board_size, pieces)
            start = time()
            if algo == '1':
                (final_state, max_states, states_expanded)  = search.bfs(initial_state)
            elif algo == '2':
                (final_state, max_states, states_expanded)  = search.dfs(initial_state)
            elif algo == '3':
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
            end = time()

            print(f'Level {i}')
            print(f'Time: {end - start:.4f}s')
            print(f'Nodes expanded: {states_expanded}')
            print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')
        
    elif difficulty == '2':
        for i in range(11,21):
            (board_size, pieces) = get_level('lvl'+str(i))
            initial_state = main.init(board_size, pieces)
            start = time()
            if algo == '1':
                (final_state, max_states, states_expanded)  = search.bfs(initial_state)
            elif algo == '2':
                (final_state, max_states, states_expanded)  = search.dfs(initial_state)
            elif algo == '3':
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
            end = time()
            
            print(f'Level {i}')
            print(f'Time: {end - start:.4f}s')
            print(f'Nodes expanded: {states_expanded}')
            print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')
        
    elif difficulty == '3':
        for i in range(21,23):
            (board_size, pieces) = get_level('lvl'+str(i))
            initial_state = main.init(board_size, pieces)
            start = time()
            if algo == '1':
                (final_state, max_states, states_expanded)  = search.bfs(initial_state)
            elif algo == '2':
                (final_state, max_states, states_expanded)  = search.dfs(initial_state)
            elif algo == '3':
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
            end = time()
            
            print(f'Level {i}')
            print(f'Time: {end - start:.4f}s')
            print(f'Nodes expanded: {states_expanded}')
            print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')