import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOARD=[]

def get_font(size):
    return pygame.font.Font("../assets/font2.ttf", size)

def construct_board(size):
    global BOARD
    BOARD=[(1,1),(720,1),(0,0),(0,720),(0,720),(720,720),(720,720),(720,0)]
    for i in range(size, 720, size):
        BOARD.append((0,i))
        BOARD.append((720,i))

def reset_board():
    BOARD.clear

def draw_board(screen, size):
    construct_board(size)
    draw_lines(screen)
    draw_cols(screen)
    c=(size/2, 720-(size/2))
    S_TEXT = get_font(size-20).render("S", True, "Black")
    S_RECT = S_TEXT.get_rect(center=c)
    screen.blit(S_TEXT, S_RECT)
    F_TEXT = get_font(size-20).render("F", True, "Black")
    F_RECT = F_TEXT.get_rect(center=Reverse(c))
    screen.blit(F_TEXT, F_RECT)

def draw_lines(screen):
    aux=[]
    for i in range(0,len(BOARD),2):
        aux=[BOARD[i],BOARD[i+1]]
        pygame.draw.lines(screen,BLACK, False,aux,3)

def draw_cols(screen):
    aux=[]
    for i in range(0,len(BOARD),2):
        aux=[Reverse(BOARD[i]), Reverse(BOARD[i+1])]
        pygame.draw.lines(screen,BLACK, False,aux,3)

def Reverse(tuples):
    new_tup=tuples[::-1]
    return new_tup

def draw_pieces(screen, size, pieces):
    for piece in pieces:
        piece_img = pygame.image.load(piece.image)
        piece_img = pygame.transform.scale(piece_img, (size,size))
        (x,y) = piece.pos
        pygame.Surface.blit(screen, piece_img, (x*size, y*size))    
    