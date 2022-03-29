
from xmlrpc.client import Boolean
from src.draw import draw_small_board, draw_big_board
from src.pieces import *

def lvl_select(SCREEN, lvl):
    if lvl<=10:
        draw_small_board(SCREEN)
    else:
        draw_big_board(SCREEN)
    

    if lvl==1:
        Rook((144,144)).draw(SCREEN ,lvl)
        King((144,144*3)).draw(SCREEN, lvl)

    elif lvl ==2:
        Knight((144,144*4)).draw(SCREEN ,lvl)
        Bishop((144*2,144)).draw(SCREEN, lvl)

    elif lvl ==3:
        Queen((0,0)).draw(SCREEN ,lvl)
        Rook((144,144*4)).draw(SCREEN, lvl)

    elif lvl ==4:
        Bishop((144,144)).draw(SCREEN ,lvl)
        King((144*2,144*2)).draw(SCREEN, lvl)

    elif lvl ==5:
        Queen((144,144)).draw(SCREEN ,lvl)
        Knight((144*3,144*4)).draw(SCREEN, lvl)

    elif lvl ==6:
        Rook((144*4,144*3)).draw(SCREEN ,lvl)
        Bishop((144*2,144*4)).draw(SCREEN, lvl)

    elif lvl ==7:
        Knight((144*3,144)).draw(SCREEN ,lvl)
        King((144*4,144*3)).draw(SCREEN, lvl)

    elif lvl ==8:
        Queen((144,144*2)).draw(SCREEN ,lvl)
        Bishop((144*4,144)).draw(SCREEN, lvl)

    elif lvl ==9:
        Rook((144*4,144*3)).draw(SCREEN ,lvl)
        Knight((144*4,144*4)).draw(SCREEN, lvl)

    elif lvl ==10:
        Queen((144,144*4)).draw(SCREEN ,lvl)
        King((144,0)).draw(SCREEN, lvl)

    elif lvl ==11:
        Queen((120*5,120*5)).draw(SCREEN ,lvl)
        Bishop((120*4,120)).draw(SCREEN, lvl)
        Rook((120*2, 120*5)).draw(SCREEN, lvl)

    elif lvl ==12:
        Knight((120*3,120*3)).draw(SCREEN ,lvl)
        King((120*2,120*4)).draw(SCREEN, lvl)
        Rook((0, 120*3)).draw(SCREEN, lvl)

    elif lvl ==13:
        Queen((120*4,120*4)).draw(SCREEN ,lvl)
        Bishop((120*4,120)).draw(SCREEN, lvl)
        Knight((120, 120*2)).draw(SCREEN, lvl)

    elif lvl ==14:
        Queen((120*2,0)).draw(SCREEN ,lvl)
        King((120*4,120*3)).draw(SCREEN, lvl)
        Rook((120*5, 120)).draw(SCREEN, lvl)

    elif lvl ==15:
        King((120,120*5)).draw(SCREEN ,lvl)
        Bishop((0,120*2)).draw(SCREEN, lvl)
        Rook((120*4, 120*3)).draw(SCREEN, lvl)

    elif lvl ==16:
        Queen((120*3,0)).draw(SCREEN ,lvl)
        Knight((120*3,120*3)).draw(SCREEN, lvl)
        Rook((120*2, 120*4)).draw(SCREEN, lvl)

    elif lvl ==17:
        King((120*3,0)).draw(SCREEN ,lvl)
        Bishop((120*4,120*3)).draw(SCREEN, lvl)
        Knight((120*2, 120*4)).draw(SCREEN, lvl)

    elif lvl ==18:
        King((120*3,120*4)).draw(SCREEN ,lvl)
        Bishop((120*4,120)).draw(SCREEN, lvl)
        Queen((120, 120)).draw(SCREEN, lvl)

    elif lvl ==19:
        Knight((120*2,120)).draw(SCREEN ,lvl)
        Bishop((0,120*2)).draw(SCREEN, lvl)
        Rook((120*4, 120*4)).draw(SCREEN, lvl)
    else:
        King((120*2,120*3)).draw(SCREEN ,lvl)
        Knight((120,120*2)).draw(SCREEN, lvl)
        Queen((120*2, 120*5)).draw(SCREEN, lvl)

