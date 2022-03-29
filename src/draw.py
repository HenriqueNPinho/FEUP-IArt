import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_BIG=[(1,1),(480,1),(0,0),(0,480),(0,480),(480,480),(480,480),(480,0)]
BOARD_SMALL=[(1,1),(480,1),(0,0),(0,480),(0,480),(480,480),(480,480),(480,0)]

for i in range(80,480,80):
    BOARD_BIG.append((0,i))
    BOARD_BIG.append((480,i))

for i in range(96,480,96):
    BOARD_SMALL.append((0,i))
    BOARD_SMALL.append((480,i))

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


    