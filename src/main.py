from draw import draw_big_board, draw_small_board
from piece import *
import utils
import pygame
import pygame_menu 


board = [
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ']
]

def print_header():
    header = ''' ___________________'''
    print(header)

def print_board(board):
    print_header()
    for row in board:
        print('|', end='')
        for col in row:
            print(col + ' |', end='')
        print('\n---------------------') 


def remove_moves(piece):
    for move in list(piece.moves):
        if move[0] < 0 or move[1] < 0:
            piece.moves.remove(move)
            continue
        if move[0] > 4 or move[1] > 4:
            piece.moves.remove(move)


        

def main():
    
    playing =True
    pygame.init()

    screen = pygame.display.set_mode(utils.GAME_WINDOW_SIZE)
    pygame.display.set_caption('Chess Snake')
    print_board(board)
    print(utils.BOARD_SMALL)
    rook = Rook((2, 3))
    bishop = Bishop((3, 1))
    king = King (1,1)
    queen = Queen(4,2)
    knight = Knight(0,4)
    pieces = [rook, bishop, king, queen, knight]

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
                   

   ##for piece in pieces:
    #    if type(piece).__name__ != 'King' and type(piece).__name__ != 'Knight':
    #        for i in range(1, 5):
    #            piece.set_moves(i)
     #    else:
      #      piece.set_moves()
       # remove_moves(piece)
        #print(type(piece).__name__, piece.moves) 
        

if __name__ == "__main__":
    main()