
import sys
from time import time

import pygame
from draw import draw_board, draw_path, draw_pieces
from file import get_level
import main
import search

def solve_gui(state, screen, square_size, pieces):
    screen.fill("White")
    screen.blit(pygame.image.load("../assets/Background.png"), (720, 0)) 
    draw_path(screen, state.get_path(), square_size)
    draw_board(screen, square_size)
    draw_pieces(screen, square_size, pieces)
    pygame.display.update()

def solve_all_puzzles(difficulty, algo):
    if difficulty == '9':
        #f = open('data.csv', 'w')
        #writer = csv.writer(f)
        for i in range(1,23):
            (board_size, pieces) = get_level('lvl'+str(i))
            initial_state = main.init(board_size, pieces)
            times = []
            max = []
            states = []
            for j in range(1,6):
                start = time()
                if j == 1:
                    print('BFS')
                    (final_state, max_states, states_expanded)  = search.bfs(initial_state)
                elif j == 2:
                    print('DFS')
                    (final_state, max_states, states_expanded)  = search.dfs(initial_state)
                elif j == 3:
                    print('A* n_hits')
                    initial_state.heuristic = 1
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                elif j == 4:
                    print('A* manhattam')
                    initial_state.heuristic = 2
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                elif j == 5:
                    print('A* n_hits+manhattam')
                    initial_state.heuristic = 3
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                end = time()

                times.append(end-start)
                max.append(max_states*sys.getsizeof(final_state)/1000)
                states.append(states_expanded)

                print(f'Level {i}')
                print(f'Time: {end - start:.4f}s')
                print(f'Nodes expanded: {states_expanded}')
                print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')


            
            #writer.writerow(times)
            #writer.writerow(max)
            #writer.writerow(states)
            #performance.draw_chart_time(len(initial_state.board), times, i)
            #performance.draw_chart_max(len(initial_state.board), max, i)
            #performance.draw_chart_expanded(len(initial_state.board), states, i)
        #f.close()
                
    if difficulty == '0':
        for i in range(1, 6):
            if i == 1:
                print('BFS\n')
            elif i == 2:
                print('DFS\n')
            elif i == 3:
                print('A* - n_hits\n')
            elif i == 4:
                print('A* - manhattam\n')
            elif i == 5:
                print('A* - n_hits+manhattam\n')
            for j in range(1, 23):
                (board_size, pieces) = get_level('lvl'+str(j))
                initial_state = main.init(board_size, pieces)
                start = time()
                if i == 1:
                    (final_state, max_states, states_expanded)  = search.bfs(initial_state)
                elif i == 2:
                    (final_state, max_states, states_expanded)  = search.dfs(initial_state)
                elif i == 3:
                    initial_state.heuristic = 1
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                    print('Heuristic: n_hits')
                elif i == 4:
                    initial_state.heuristic = 2
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                    print('Heuristic: manhattam')
                elif i == 5:
                    initial_state.heuristic = 3
                    (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                    print('Heuristic: n_hits+manhattam')
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
                initial_state.heuristic = 1
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: n_hits')
            elif algo == '4':
                initial_state.heuristic = 2
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: manhattam')
            elif algo == '5':
                initial_state.heuristic = 3
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: n_hits+manhattam')
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
                initial_state.heuristic = 1
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: n_hits')
            elif algo == '4':
                initial_state.heuristic = 2
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: manhattam')
            elif algo == '5':
                initial_state.heuristic = 3
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: n_hits+manhattam')
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
                initial_state.heuristic = 1
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: n_hits')
            elif algo == '4':
                initial_state.heuristic = 2
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: manhattam')
            elif algo == '5':
                initial_state.heuristic = 3
                (final_state, max_states, states_expanded)  = search.a_star(initial_state)
                print('Heuristic: n_hits+manhattam')
            end = time()
            
            print(f'Level {i}')
            print(f'Time: {end - start:.4f}s')
            print(f'Nodes expanded: {states_expanded}')
            print(f'Max Memory: {max_states*sys.getsizeof(final_state)/1000} KB\n\n')