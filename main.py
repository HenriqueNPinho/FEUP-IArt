import pygame, sys
from src.levels import *
from src.button import Button
from src.draw import draw_big_board, draw_small_board
from src.pieces import *

pygame.init()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Chess Snake Puzzles")
pygame.display.set_icon(pygame.image.load("pieces/king.png"))
BG = pygame.image.load("assets/Background.png") #mudar imagem
i=1

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():

    playing=True
    while(playing):
        clock.tick(30)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("White")
        SCREEN.blit(BG, (720, 0))

        lvl_select(SCREEN, i)
       

        PLAY_BACK = Button(image=None, pos=(1000, 660), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")
        for button in [PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    choose_lvl()
                    playing=False
        pygame.display.update()


def show_lvl():
    lvl_img = pygame.image.load("lvls/"+str(i)+".png")
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

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Game Rules", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
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