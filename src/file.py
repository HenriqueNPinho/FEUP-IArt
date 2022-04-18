from pieces import *

def get_level(lvl):
    f = open('puzzles/'+lvl, 'r')
    board_size = int(f.readline())
    pieces = []
    for line in f:
        pieces.append(get_piece(board_size, line))
    return (board_size, pieces)



def get_piece(board_size, line):
    [piece_name, pos_x, pos_y] = line.split()
    x = int(pos_x)
    y = int(pos_y)
    
    if piece_name == 'King':
        piece = King((x,y), board_size)

    elif piece_name == 'Rook':
        piece = Rook((x,y), board_size)

    elif piece_name == 'Queen':
        piece = Queen((x,y), board_size)

    elif piece_name == 'Bishop':
        piece = Bishop((x,y), board_size)

    elif piece_name == 'Knight':
        piece = Knight((x,y), board_size)
    
    return piece
