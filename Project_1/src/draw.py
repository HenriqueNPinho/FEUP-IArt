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

def draw_main_piece(screen, pos):
    pygame.draw.circle(screen, (10, 10, 10),( pos[0] , pos[1]),40)

def draw_path(screen, path, square_size):
    for i in range(0,len(path)-1, 1):
        (x,y,_)=path[i]
        pygame.draw.rect(screen, (128, 128, 128), (x*square_size, y*square_size, square_size , square_size),0)

def draw_legal_moves(screen, square_size, pos):
    for p in pos:
        pygame.draw.circle(screen, (0,255,0),
                         ( square_size/2 + (p[0])*square_size,   ( square_size*((p[1]+1)*2-1) ) /2 ), 10)