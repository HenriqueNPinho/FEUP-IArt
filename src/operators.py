from state import State


def get_new_state(state, dir):
    current_pos = state.pos
    if dir == 'U':
        next_pos = (current_pos[0], current_pos[1] - 1)
    elif dir == 'D':
        next_pos = (current_pos[0], current_pos[1] + 1)
    elif dir == 'L':
        next_pos = (current_pos[0] - 1, current_pos[1])
    elif dir == 'R':
        next_pos = (current_pos[0] + 1, current_pos[1])

    return State(next_pos, state.board, state.pieces, dir, state, state.depth + 1)


def valid_state(state):
    (x, y) = state.pos
    board = state.board
    pieces = state.pieces

    if not(0 <= x < len(board) and 0 <= y < len(board)):
            return False

    for piece in pieces:
        if piece.pos == state.pos:
            return False

    return is_valid(state.get_path())


def is_valid(path):
    (x,y,d) = path[-1]

    for i in range(0, len(path)-1):
        (a,b,_) = path[i]

        if (x,y) == (a,b):
            return False
        if d == 'R':
            if (a, b) in [(x, y+1), (x, y-1), (x+1, y), (x+1, y-1), (x+1, y+1)]:
                return False
        elif d == 'L':
            if (a, b) in [(x, y-1), (x, y+1), (x-1, y), (x-1, y-1), (x-1, y+1)]:
                return False
        elif d == 'U':
            if (a, b) in [(x+1, y), (x-1, y), (x, y-1), (x+1, y-1), (x-1, y-1)]:
                return False
        elif d == 'D':
            if (a, b) in [(x+1, y), (x-1, y), (x-1, y+1), (x+1, y+1), (x, y+1)]:
                return False
    return True


def end_state(state):
    final_pos = (len(state.board) - 1, 0)

    if state.pos != final_pos:
        return False

    return equal_final_hits(state)
       

def equal_final_hits(state):
    hits = state.get_pieces_hits()
    return all(hit == hits[0] for hit in hits)