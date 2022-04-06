class State:
    def __init__(self, pos, board, pieces, dir = 'S', parent_node = None, depth = 0):
        self.pos = pos
        self.board = board
        self.dir = dir
        self.parent_node = parent_node
        self.depth = depth
        self.pieces = pieces
        self.pieces_hits = self.__set_hits()

    def move(self, dir):
        current_pos = self.pos
        if dir == 'U':
            next_pos = (current_pos[0], current_pos[1] - 1)
        elif dir == 'D':
            next_pos = (current_pos[0], current_pos[1] + 1)
        elif dir == 'L':
            next_pos = (current_pos[0] - 1, current_pos[1])
        elif dir == 'R':
            next_pos = (current_pos[0] + 1, current_pos[1])

        return State(next_pos, self.board, self.pieces, dir, self, self.depth + 1)

    def get_path(self):
        path = [(self.pos[0], self.pos[1], self.dir)]
        parent_node = self.parent_node
        while parent_node != None:
            path = [(parent_node.pos[0], parent_node.pos[1], parent_node.dir)] + path
            parent_node = parent_node.parent_node
        return path

    def get_pieces_hits(self):
        return list(self.pieces_hits.values())

    def __set_hits(self):
        pieces_hits = {}
        i = 0
        if self.parent_node != None:
            for piece in self.pieces:
                piece_name = type(piece).__name__ + '_' + str(i)
                pieces_hits[piece_name] = self.parent_node.pieces_hits[piece_name]
                for piece_move in piece.moves:
                    if piece_move == self.pos:
                        pieces_hits[piece_name] = self.parent_node.pieces_hits[piece_name] + 1
                i += 1
        else:
            for piece in self.pieces:
                piece_name = type(piece).__name__ + '_' + str(i)
                pieces_hits[piece_name] = 0
                for piece_move in piece.moves:
                    if piece_move == self.pos:
                        pieces_hits[piece_name] = 1
                i += 1
        return pieces_hits

