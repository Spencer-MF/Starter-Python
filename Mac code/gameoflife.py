GAME_SIZE = 10
GAME_SIZE_X = GAME_SIZE
GAME_SIZE_Y = GAME_SIZE

class game_set():

    def __init__(self):
        self.game_board = {}
        self.setup_row = []
        self.setup_col = []

    def gameboard_handler(self):
        row = []
        for i in range(GAME_SIZE_Y):
            for j in range(GAME_SIZE_X):
                row.append(0)
            self.game_board[i] = row
            row = []     

    def setup_condition(self):
        self.setup_col = []
        self.setup_row = []
        while True:
            print('input in pairs')
            c = int(input('Column you want to be on\n'))
            r = int(input('Row you want to be on\n'))
            self.setup_col.append(c)
            self.setup_row.append(r)
            out = input('would you like to end?\npress e to end\n')
            if out == 'e':
                break
        self.setup()
            
    
    def setup(self):
        for i in range(len(self.setup_row)):
            row = self.game_board[self.setup_row[i]]
            row[self.setup_col[i]] = 1
            self.game_board[self.setup_col[i]] = row
        print(self.game_board)      

    def start(self):
        self.gameboard_handler()
        self.setup_condition()

class logic():

    def __init__(self, gs):
        self.gs = gs

        self.current_board = {}
        self.future_board = {}

    def game(self):
        self.import_board()
        for i in range(3):
            self.main_loop()
    
    def import_board(self):
        self.current_board = gs.game_board

    def main_loop(self):
        self.check_board()
        self.update_board()
        self.display_board()

    def check_board(self):
        for rows in self.current_board.keys():
            row = self.current_board[rows]
            for i in range(len(row)):
                n = self.board_check(rows, i)
                self.next_board_state(rows, i, n)
    
    def board_check(self, off_set_x, off_set_y):
        n_count = 0
        for i in range(3):
            for j in range(3):
                in_bounds, r, c = self.rectify(i,j ,off_set_x, off_set_y)
                if in_bounds:
                    if self.cell_check(r,c):
                        n_count += 1
        in_bounds, r, c = self.rectify(1, 1, off_set_x, off_set_y)
        if in_bounds and self.cell_check(r,c):
            n_count -= 1
        return n_count
    
    def cell_check(self, row, col):
        r = self.current_board[col]
        if r[row] == 1:
            return True
        else:
            return False 
    
    def rectify(self, i, j, r, c):
        sudo_bool = 0
        row = i-1+r
        col = j-1+c
        if row > -1 and row < GAME_SIZE_X:
            sudo_bool += 1
        if col > -1 and col < GAME_SIZE_Y:
            sudo_bool += 1
        if sudo_bool == 2:
            return True, row, col
        else:
            return False, None, None
        
    def next_board_state(self, row, col, n):
        if n < 2 or n > 3:
            self.dead(row, col)
        else:
            self.live(row, col)
    
    def dead(self, row, col):
        r = self.current_board[col]
        r[row] = 0
        self.future_board[col] = r

    def live(self, row, col):
        r = self.current_board[col]
        r[row] = 1
        self.future_board[col] = r

    def update_board(self):
        self.current_board = self.future_board

    def display_board(self):
        print(self.current_board)

class screen():

    def __init(self, lg):
        self.lg = lg

gs = game_set()
lg = logic(gs)
sc = screen(lg)

def main():
    gs.start()
    lg.game()

main()