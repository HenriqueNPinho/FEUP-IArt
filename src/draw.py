import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD_BIG=[(1,1),(720,1),(0,0),(0,720),(0,720),(720,720),(720,720),(720,0)]
BOARD_SMALL=[(1,1),(720,1),(0,0),(0,720),(0,720),(720,720),(720,720),(720,0)]

def get_font(size):
    return pygame.font.Font("assets/font2.ttf", size)

for i in range(120,720,120):
    BOARD_BIG.append((0,i))
    BOARD_BIG.append((720,i))

for i in range(144,720,144):
    BOARD_SMALL.append((0,i))
    BOARD_SMALL.append((720,i))

def draw_big_board(screen):
    draw_lines(screen, BOARD_BIG)
    draw_cols(screen, BOARD_BIG)
    S_TEXT = get_font(100).render("S", True, "Black")
    S_RECT = S_TEXT.get_rect(center=(60, 660))
    screen.blit(S_TEXT, S_RECT)
    F_TEXT = get_font(100).render("F", True, "Black")
    F_RECT = F_TEXT.get_rect(center=(660, 60))
    screen.blit(F_TEXT, F_RECT)


def draw_small_board(screen):
    draw_lines(screen, BOARD_SMALL)
    draw_cols(screen, BOARD_SMALL)
    S_TEXT = get_font(120).render("S", True, "Black")
    S_RECT = S_TEXT.get_rect(center=(72, 648))
    screen.blit(S_TEXT, S_RECT)
    F_TEXT = get_font(120).render("F", True, "Black")
    F_RECT = F_TEXT.get_rect(center=(648, 72))
    screen.blit(F_TEXT, F_RECT)



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


    