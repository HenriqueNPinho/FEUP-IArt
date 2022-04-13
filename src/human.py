from queue import Queue
from main import main, bfs, get_new_state, valid_state, draw_board

def get_human_move(pos):
    move='N'
    while move not in pos:
        print("available moves: ")
        print(pos)
        move=input("Select ur move: ")
    return move
    

def human(initial_state):
    
    states = Queue()
    states.put(initial_state)
    current_state = initial_state
    objective_state=bfs(initial_state)
    board = initial_state.board
    
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

        current_state = get_new_state(current_state, dir)

    print("You Won \n")
    main()