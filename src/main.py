from piece import * 
from snake import *
from state import *

board_size = 5

board = [[' ']*board_size for _ in range(board_size)]

def print_board(board):
    print('________________')
    for row in board:
        print('|', end='')
        for col in row:
            print(col + ' |', end='')
        print('\n---------------------') 

def set_pieces_moves(pieces):
    for piece in pieces:
        if type(piece).__name__ != 'King' and type(piece).__name__ != 'Knight':
            for i in range(1, board_size):
                piece.set_moves(i)
        else:
            piece.set_moves()
        remove_unnecessary_moves(piece)

def remove_unnecessary_moves(piece):
    for move in list(piece.moves):
        if move[0] < 0 or move[1] < 0:
            piece.moves.remove(move)
            continue
        if move[0] > board_size-1 or move[1] > board_size-1:
            piece.moves.remove(move)
        

def main():
    #print_board(board)

    rook = Rook((1, 1))
    #bishop = Bishop((3, 1))
    king = King((1,3))
    #queen = Queen((4,2))
    #knight = Knight((1,3))

    pieces = [rook, king]

    snake = Snake(board_size)

    state = State(snake,board,pieces)

    state.print(board, pieces, snake)
        
        


if __name__ == "__main__":
    main()