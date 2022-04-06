
def print_board(board, pieces):
        x = 0
        y = 0
        for row in board:
            print('|', end='')
            for col in row:
                for piece in pieces:
                    if piece.pos is (x,y):                        
                        col = piece.symbol
                
                print(col + ' |', end='')
                x = x+1
            x = 0
            y = y+1
            print('\n' + '-'*16)

def same_score(pieces):
    scores = []
    for piece in pieces:
        scores.append(piece.score)
    return all(score == scores[0] for score in scores)


def draw_board(board, pieces, moves=''):
    x = 0
    y = len(board)-1
    pos = set()
    pos.add((x,y))
    for move in moves:
        if move == 'U':
            y-=1
        if move == 'D':
            y+=1
        if move == 'R':
            x+=1
        if move == 'L':
            x-=1
        pos.add((x,y))
    print('___'*board_size)
    for x, row in enumerate(board):
        print('|',end='')
        for y, col in enumerate(row):
            if (y,x) in pos:
                print('+ ', end='')
            else:
                for piece in pieces:
                    if piece.pos == (y,x):
                        col = piece.symbol
                print(col + ' ', end='')
            print('|',end='')
        print()
        print('---'*board_size)



def valid(board, pieces, moves):
    x = 0
    y = len(board)-1

    path = [(x,y,'S')]

    for move in moves:
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1

        path.append((x,y,move))

        if not(0 <= x < len(board) and 0 <= y < len(board)):
            return False

        for piece in pieces:
            if (x,y) == piece.pos:
                return False   

    if not is_valid(path):
        return False
            
    return True


def remove_more_moves(board, piece, pos):
    (x,y) = tuple(np.subtract(piece.pos,pos))

    if x == 0 and y < 0:
        for i in range(pos[1]+1,len(board)):
            for move in list(piece.moves):
                if move == (pos[0],i):
                    piece.moves.remove(move)



def bfs(board, pieces):
    moves = Queue()
    moves.put("")
    add = ""

    while not end(board, pieces, add): 
        add = moves.get()
        #print(add)
        for d in ['L', 'R', 'U', 'D']:
            move = add + d
            if valid(board, pieces, move):
                
                moves.put(move)


def count_score(x,y,pieces):
    for piece in pieces:
            for piece_move in piece.moves:
                    if (x,y) == piece_move:
                        piece.score +=1




def end(board, pieces, moves):
    x = 0
    y = len(board) - 1
    
    count_score(x,y,pieces)

    for move in moves:
        if move == 'U':
            y-=1
        elif move == 'D':
            y+=1
        elif move == 'L':
            x-=1
        elif move == 'R':
            x+=1
            
        count_score(x,y,pieces)       

    if ((x,y) == (len(board)-1,0) and same_score(pieces)):
        print('Solution:', moves)
        draw_board(board, pieces, moves)
        return True
        
    reset_score(pieces)
    return False

def reset_score(pieces):
    for piece in pieces:
        piece.score = 0

def read_file(file):
    f = open(file, 'r')
    board = f.readlines()
    return board