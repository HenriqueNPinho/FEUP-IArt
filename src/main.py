import enum
from pieces import *
from draw import draw_big_board, draw_small_board
import utils
import pygame
import queue
import pygame_menu 

board_size = 5

board = [[' ']*board_size for _ in range(board_size)]

def print_board(board, pieces):
        x = 0
        y = 0
        for row in board:
            print('|', end='')
            for col in row:
                for piece in pieces:
                    if piece.pos is (x,y):                        
                        col = piece.symbol
                
                print(col + ' |', end='')
                x = x+1
            x = 0
            y = y+1
            print('\n' + '-'*16)

def draw_board(board, moves=""):
    x = 0
    y = len(board)-1
    pos = set()
    pos.add((x,y))
    for move in moves:
        if move == 'U':
            y-=1
        if move == 'D':
            y+=1
        if move == 'R':
            x+=1
        if move == 'L':
            x-=1
        pos.add((x,y))

    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if (x,y) in pos:
                print('+ ', end='')
            else:
                print(col + ' ', end='')
        print()


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


def same_score(pieces):
    scores = []
    for piece in pieces:
        scores.append(piece.score)
    return all(score == scores[0] for score in scores)


def valid(board, pieces, moves):
    x = 0
    y = len(board)-1

    for move in moves:
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1

        if not(0 <= x < len(board) and 0 <= y < len(board)):
            return False

        for piece in pieces:
            if (x,y) == piece.pos:
                return False
            for piece_move in piece.moves:
                if (x,y) == piece_move:
                    piece.score +=1

        return True




def bfs(board, pieces):
    nums = queue.Queue()
    nums.put("")
    add = ""

    while not end(board, pieces, add): 
        add = nums.get()
        #print(add)
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(board, pieces, put):
                nums.put(put)


def end(board, pieces, moves):
    x = 0
    y = len(board) - 1
    for move in moves:
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1

    if ((x,y) == (len(board)-1,0)):
        print('End:', moves)
        draw_board(board, moves)
        return True
    reset_score(pieces)
    return False

def reset_score(pieces):
    for piece in pieces:
        piece.score = 0

def read_file(file):
    f = open(file, 'r')
    board = f.readlines()
    return board

def main():
    #print_board(board)

    board = read_file('lvl1.txt')
    print(board)


    rook = Rook((1, 1))
    #bishop = Bishop((2, 1))
    king = King((1,3))
    #queen = Queen((0,0))
    #knight = Knight((2,4))

    pieces = [king, rook]

    set_pieces_moves(pieces)

    print_board(board, pieces)


    bfs(board, pieces)

    
        
    
    playing =True
    pygame.init()

    screen = pygame.display.set_mode(utils.GAME_WINDOW_SIZE)
    pygame.display.set_caption('Chess Snake')
    #print_board(board)
    print(utils.BOARD_SMALL)

    screen.fill(utils.GAME_WINDOW_COLOR)
    ##6x6
    #draw_big_board(screen)
    ##5x5
    draw_small_board(screen)
    pygame.display.update()


    while(playing):

   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             playing = False
        



    

if __name__ == "__main__":
    main()

