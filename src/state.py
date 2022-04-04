class State:
    def __init__(self, pos, board, pieces, dir = 'S', parent_node = None, depth = 0):
        self.pos = pos
        self.board = board
        self.dir = dir
        self.parent_node = parent_node
        self.depth = depth
        self.pieces = pieces
        self.pieces_hits = self.__set_pieces_hits()

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

    def __update_pieces(self, pieces):
        new_pieces = []

        for piece in pieces:
            score = 0
            for move in piece.moves:
                if move == self.pos:
                    score += 1
            new_pieces.append((piece, score))

        return new_pieces

    def __set_scores(self):
        scores = []
        if not hasattr(self, 'scores'):
            score = 0
            for piece in self.pieces:
                for move in piece.moves:
                    if move == self.pos:
                        score += 1
                scores.append((piece, score))
        else:
            scores = self.scores
            i = 0
            for piece in self.pieces:
                for move in piece.moves:
                    if move == self.pos:
                        scores[i][1] += 1
                i += 1
            
        return scores

    def __set_pieces_hits(self):
        pieces_hits = {}
        piece_move_found = False

        for piece in self.pieces:
            for piece_move in piece.moves:
                if piece_move == self.pos:
                    pieces_hits[piece] = 1
                    piece_move_found = True
            if not piece_move_found:
                pieces_hits[piece] = 0
            piece_move_found = False

        return pieces_hits


    def get_path(self):
        path = [(self.pos[0], self.pos[1], self.dir)]
        parent_node = self.parent_node
        while parent_node != None:
            path = [(parent_node.pos[0], parent_node.pos[1], parent_node.dir)] + path
            parent_node = parent_node.parent_node
        return path

    def get_pieces_hits(self):
        pieces_hits = self.pieces_hits
        hits = [0] * len(pieces_hits)
        parent_node = self.parent_node

        while parent_node != None:
            i = 0
            for piece in self.pieces:
                hits[i] += pieces_hits[piece]
                i += 1
            pieces_hits = parent_node.pieces_hits
            parent_node = parent_node.parent_node

        i = 0
        for piece in self.pieces:
            if parent_node == None:
                hits[i] += pieces_hits[piece]    
            i += 1
            
        return hits
