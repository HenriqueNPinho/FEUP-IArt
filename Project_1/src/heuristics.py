def manhattan(pos, final_pos):
    (x, y) = pos
    (x1, y1) = final_pos

    return (x1-x) + (y-y1)


def n_hits(state):
    pieces_hits = state.get_pieces_hits()
    min = pieces_hits[0]
    max = pieces_hits[0]
    
    for piece_hit in pieces_hits:
        if piece_hit < min:
            min = piece_hit
        if piece_hit > max:
            max = piece_hit

    return (max-min)