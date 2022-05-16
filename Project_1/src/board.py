def draw_board(state):
    board = state.board
    pieces = state.pieces
    path = state.get_path()
    board_size = len(board)

    pos = []

    for p in path:
        (a,b,_) = p
        pos.append((a,b))

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