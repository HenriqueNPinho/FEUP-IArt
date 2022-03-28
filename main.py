
from glob import glob
import pygame, sys
from src.button import Button
from src.draw import draw_big_board, draw_small_board
from src.piece import *
import utils
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Chess Snake Puzzles")
pygame.display.set_icon(pygame.image.load("pieces/king.png"))
BG = pygame.image.load("assets/Background.png")
i=0
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def show_lvl():
    LVL_TEXT = get_font(45).render("cona", True, "white")
    LVL_RECT = LVL_TEXT.get_rect(center=(640, 160))
    SCREEN.blit(LVL_TEXT, LVL_RECT)

def play():
    playing =True
    
    while(playing):

        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
      # SCREEN.fill((255,255,255))
        global i
        show_lvl()
        OPTIONS_TEXT = get_font(45).render("Level "+str(i), True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 560))
       

        PLAY_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")
    
        NEXT_LVL = Button(image=None, pos=(840, 560), 
                            text_input=">", font=get_font(75), base_color="white", hovering_color="Green")

        LAST_LEVEL = Button(image=None, pos=(440, 560), 
                            text_input="<", font=get_font(75), base_color="white", hovering_color="Green")
        
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
    
        for button in [PLAY_BACK, LAST_LEVEL, NEXT_LVL]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if NEXT_LVL.checkForInput(PLAY_MOUSE_POS):
                    i+=1
                    if i>20:
                        i=20
                if LAST_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    i-=1
                    if i<0:
                        i=0

        ##6x6
        #draw_big_board(screen)
        #5x5
        # draw_small_board(SCREEN)
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
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()