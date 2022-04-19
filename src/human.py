from queue import Queue
from gui import main, bfs, get_new_state, valid_state, draw_board

def get_human_move(pos):
    move=''
    while move.upper() not in pos:
        print(f"Available moves: ", pos)
        move=input("Select your move: ")
        if move == 'b':
            return move.upper()
    return move.upper()
    

def human(initial_state):
    
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    objective_state=bfs(initial_state)
    board = initial_state.board
    n_moves = 0

    
    while current_state.get_path() != objective_state.get_path():
        valid_pos=[]
        
        for d in ['L', 'R', 'U', 'D']:
            new_state = get_new_state(current_state, d)
            if valid_state(new_state):
                valid_pos.append(new_state.dir)
        
        draw_board(current_state)

        if current_state.pos == (len(board)-1, 0):
            print("Solution: ", objective_state.pieces_hits)
            print("Your play: ", current_state.pieces_hits)

        dir = get_human_move(valid_pos)

        if dir == 'B':
            if current_state.parent_node != None:
                current_state = current_state.parent_node
        else:
            current_state = get_new_state(current_state, dir)

        n_moves += 1

    print("You Won \n")
    main()