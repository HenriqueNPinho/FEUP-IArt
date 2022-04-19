from pieces import *
import search
from state import *
from file import *
import human
from board import draw_board
import sys

def main():
    if len(sys.argv) < 2:
        print('USAGE > python3 main.py <lvl>')
        return
        
    (board_size, pieces) = get_level(sys.argv[1])
    board = [[' ']*board_size for _ in range(board_size)]

    remove_pieces_moves(pieces, board_size)

    initial_pos = (0, board_size - 1)

    initial_state = State(initial_pos, board, pieces)

    menu(initial_state)


def menu(initial_state):
    print('\nCHESS SNAKE PUZZLES\n')
    print('1 - Player', '2 - CPU', '0 - Exit', sep='\n')
    aux = input('\n> ')

    if aux == '2':
        draw_board(initial_state)
        print()
        #dfs(initial_state)
        search.bfs(initial_state)
        search.a_star(initial_state)
    elif aux == '1': 
        human.human(initial_state)
    elif aux == '0':
        return

    menu(initial_state)


if __name__ == "__main__":
    main()