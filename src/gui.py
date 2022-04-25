
import pygame, sys
from file import get_level
from button import Button
from draw import *
from pieces import *
from operators import *


pygame.init()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Chess Snake Puzzles")
pygame.display.set_icon(pygame.image.load("../pieces/king.png"))
BG = pygame.image.load("../assets/Background.png") #mudar imagem
i=1

def init(board_size, pieces):
    board = [[' ']*board_size for _ in range(board_size)]

    remove_pieces_moves(pieces, board_size) # remove not valid moves

    initial_pos = (0, board_size - 1)

    return State(initial_pos, board, pieces)


def convert_to_boardPos(p, square_size):
    return (square_size/2 + (p[0])*square_size,   ( square_size*((p[1]+1)*2-1) ) /2 )

def get_dir(oldPos, newPos):
    (x,y)=oldPos
    (x1, y1) = newPos

    if(x>x1):
        return 'L'
    elif (x<x1):
        return 'R'
    elif(y>y1):
        return 'U'
    elif(y<y1): 
        return 'D'

def new_state(state, pos, dir):
    return State(pos, state.board, state.pieces, dir , state, state.depth + 1)


def valid_moves(state):
    valid_pos=[]
    
    for d in ['L', 'R', 'U', 'D']:
        new_state = get_new_state(state, d)
        
        if valid_state(new_state):
            valid_pos.append(new_state.pos)

    if state.parent_node != None :
        valid_pos.append(state.parent_node.pos) ##melhorar
    return(valid_pos)
 

def move_piece(fromPos, toPos, valid_M):
    
    for pos in valid_M:
        (x,y)=pos  
        if toPos == (x,y):
            return toPos
    return fromPos 

def convert_mouse_pos(pos,square_size):
    (x, y) = pos
    line = x  / square_size
    col = y / square_size
    return (int(line), int(col))

def get_font(size):
    return pygame.font.Font("../assets/font.ttf", size)

def play():

    PLAY_BACK = Button(image=None, pos=(1000, 660), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

    (board_size, pieces)= get_level('lvl'+str(i))
    square_size= int(720/board_size)
    player_pos=( int(square_size/2), int(( square_size*(board_size*2-1) )/2))

    playing=True
    state=init(board_size, pieces)
    pieceSelected=False

    while(playing):
        clock.tick(30)

        
        valid_M=valid_moves(state)
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")
        SCREEN.blit(BG, (720, 0))  

        draw_path(SCREEN, state.get_path(), square_size)
        draw_board(SCREEN, square_size)
        draw_pieces(SCREEN, square_size, pieces)
        draw_main_piece(SCREEN, player_pos)
        draw_legal_moves(SCREEN,square_size,valid_M)   

        for button in [PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    playing=False
                    reset_board()
                    choose_lvl()

                ##peça
                pieceSelPos = convert_mouse_pos(PLAY_MOUSE_POS, square_size)
                old_pos=convert_mouse_pos(player_pos, square_size)
                newPos=move_piece(old_pos,pieceSelPos, valid_M)

                if state.parent_node!= None and (newPos == state.parent_node.pos):
                    state= state.parent_node
                if not old_pos == newPos:  
                    state=new_state(state, newPos, get_dir(old_pos, newPos)) ## add andar p/tras; check F; butoes -> reset, algoritmos;
                    
                player_pos= convert_to_boardPos(newPos, square_size)
          
        pygame.display.update()


def show_lvl():
    lvl_img = pygame.image.load("../lvls/"+str(i)+".png")
    lvl_img = pygame.transform.scale(lvl_img, (350,350))
    SCREEN.blit(lvl_img, (470, 100))

def choose_lvl():
    choosing =True
    while(choosing):
        clock.tick(30)
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        global i
        show_lvl()

        CHOOSE_LVL = Button(image=None, pos= (640, 560), 
                            text_input="Level "+str(i), font=get_font(75), base_color="white", hovering_color="Green")

        PLAY_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")
    
        NEXT_LVL = Button(image=None, pos=(840, 560), 
                            text_input=">", font=get_font(75), base_color="white", hovering_color="Green")

        LAST_LEVEL = Button(image=None, pos=(440, 560), 
                            text_input="<", font=get_font(75), base_color="white", hovering_color="Green")
    
    
        for button in [PLAY_BACK, LAST_LEVEL, NEXT_LVL, CHOOSE_LVL]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    choosing=False
                if CHOOSE_LVL.checkForInput(PLAY_MOUSE_POS):
                    play()
                    choosing=False
                if NEXT_LVL.checkForInput(PLAY_MOUSE_POS):
                    i+=1
                    if i>20:
                        i=1
                if LAST_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    i-=1
                    if i<1:
                        i=20

        pygame.display.update()

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    menu_loop=True
    while menu_loop:
        SCREEN.blit(BG, (0, 0))
        clock.tick(30)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(150).render("MAIN   MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Game Rules", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    choose_lvl()
                    menu_loop=False
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()