import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_BIG=[(1,1),(720,1),(0,0),(0,720),(0,720),(720,720),(720,720),(720,0)]
BOARD_SMALL=[(1,1),(720,1),(0,0),(0,720),(0,720),(720,720),(720,720),(720,0)]

for i in range(120,720,120):
    BOARD_BIG.append((0,i))
    BOARD_BIG.append((720,i))

for i in range(144,720,144):
    BOARD_SMALL.append((0,i))
    BOARD_SMALL.append((720,i))

def draw_big_board(screen):
    draw_lines(screen, BOARD_BIG)
    draw_cols(screen, BOARD_BIG)

def draw_small_board(screen):
    draw_lines(screen, BOARD_SMALL)
    draw_cols(screen, BOARD_SMALL)


def draw_lines(screen,board):
    aux=[]
    for i in range(0,len(board),2):
        aux=[board[i],board[i+1]]
        pygame.draw.lines(screen,BLACK, False,aux,3)

def draw_cols(screen,board):
    aux=[]
    for i in range(0,len(board),2):
        aux=[Reverse(board[i]), Reverse(board[i+1])]
        pygame.draw.lines(screen,BLACK, False,aux,3)

def Reverse(tuples):
    new_tup=tuples[::-1]
    return new_tup


    