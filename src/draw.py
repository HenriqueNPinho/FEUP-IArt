import utils
import pygame

def draw_big_board(screen):
    draw_lines(screen, utils.BOARD_BIG)
    draw_cols(screen, utils.BOARD_BIG)

def draw_small_board(screen):
    draw_lines(screen, utils.BOARD_SMALL)
    draw_cols(screen, utils.BOARD_SMALL)


def draw_lines(screen,board):
    aux=[]
    for i in range(0,len(board),2):
        aux=[board[i],board[i+1]]
        pygame.draw.lines(screen,utils.BLACK, False,aux,3)

def draw_cols(screen,board):
    aux=[]
    for i in range(0,len(board),2):
        aux=[Reverse(board[i]), Reverse(board[i+1])]
        pygame.draw.lines(screen,utils.BLACK, False,aux,3)

def Reverse(tuples):
    new_tup=tuples[::-1]
    return new_tup


    