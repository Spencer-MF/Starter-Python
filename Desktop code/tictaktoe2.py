import tkinter as tk
import random

CANVAS_SIZE = 750
SQUARE_SIZE = CANVAS_SIZE // 3
IN_BOARDER = 10
TEXT_SIZE = CANVAS_SIZE // 11

class ttoLogic:

    def __init__(self, root):
        self.x = None
        self.y = None
        self.turn = 0

        self.objs_x = []
        self.objs_o = []


        self.pos_x = []
        self.pos_o = []
        self.pos_o_over_flow = []
        self.empty_pos = [1,2,3,4,5,6,7,8,9]

        self.theme = 0

        self.bg = 'white'
        self.grid = 'black'
        self.x_color = 'red'
        self.o_color = 'blue'
        self.o_in_fill = self.bg
        self.txt_color = self.grid
        self.win_line = 'lime'

        self.redraw = False

        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, background=self.bg)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.input_sqare)
        root.bind('<Key-r>', self.reset)
        root.bind('<Key-R>', self.reset)
        root.bind('<Key-a>', self.play_AI)
        root.bind('<Key-A>', self.play_AI)
        root.bind('<Key-m>', self.mode)
        root.bind('<Key-M>', self.mode)
        root.bind('<Key-t>', self.themes)
        root.bind('<Key-T>', self.themes)

        self.playing_AI = False
        self.game_mode = 0
        self.normal_game_mode = True
        self.peices_allowed = 7
        self.AI_turns = 1

        self.game()
        self.turns_pvp()
        self.turns_pve()
        self.game_won = False

    def input_sqare(self, event):
        self.x = event.x // SQUARE_SIZE
        self.y = event.y // SQUARE_SIZE

        if not self.playing_AI:
            self.turns_pvp()
        else:
            self.turns_pve()

    def play_AI(self, event=None):
        if self.playing_AI:
            self.playing_AI = False
        else:
            self.playing_AI = True
    
    def mode(self, event=None):
        if self.game_mode == 0:
            self.game_mode = 1
            self.normal_game_mode = False
        else:
            self.game_mode = 0
            self.normal_game_mode = True
    
    def themes(self, event=None):
        if self.theme == 0:
            self.bg = 'black'
            self.grid = 'white'
            self.o_in_fill = self.bg
            self.txt_color = self.grid
            self.theme = 1
        elif self.theme == 1:
            self.bg = 'white'
            self.grid = 'black'
            self.o_in_fill = self.bg
            self.txt_color = self.grid
            self.theme = 0
        
        self.canvas.delete('all')
        if len(self.pos_o) > 0:
            self.redraw = True
            for i in range(len(self.pos_o)):
                rc = self.pos_o[i]
                c = (rc - 1) % 3
                r = (rc - 1) // 3
                self.circle(c, r)
        if len(self.pos_x) > 0:
            self.redraw = True
            for i in range(len(self.pos_x)):
                rc = self.pos_x[i]
                c = (rc - 1) % 3
                r = (rc - 1) // 3
                self.cross(c, r)
        self.redraw = False

        if self.game_won:
            self.win()

        self.canvas.config(bg=self.bg)
        self.play_grid()
        self.canvas.update_idletasks()

    def turns_pvp(self):
        if self.x is not None and self.y is not None:
            whos_turn = self.turn
            whos_turn %= 2
            if whos_turn == 0:
                self.turn += 1
                self.cross(self.x, self.y)
            else:
                self.turn += 1
                self.circle(self.x, self.y)
        self.game_win()
        if self.game_won:
            self.win()
        elif len(self.empty_pos) == 0:
            self.draw()

    def turns_pve(self):
        if self.x is not None and self.y is not None:
            whos_turn = self.turn
            whos_turn %= 2
            if whos_turn == 0:
                self.turn += 1
                self.cross(self.x, self.y)
                self.AI_turns += 1
            else:
                self.turn += 1
                x, y = self.eval()
                self.circle(x, y)
        self.game_win()
        if self.game_won:
            self.win()
        elif len(self.empty_pos) == 0:
            self.draw()
        elif self.AI_turns % 2 == 0:
            self.turns_pve()

    def board_state(self):
        used_pos = (self.pos_o + self.pos_x)
        for num in used_pos:
            if num in self.empty_pos:
                self.empty_pos.remove(num)

    def game(self):
        self.play_grid()

    def game_win(self):
        r1 = [1,2,3]
        r2 = [4,5,6]
        r3 = [7,8,9]
        c1 = [1,4,7]
        c2 = [2,5,8]
        c3 = [3,6,9]
        d1 = [1,5,9]
        d2 = [3,5,7]
        if any(set(combination).issubset(set(self.pos_x)) for combination in [r1, r2, r3, c1, c2, c3, d1, d2]):
            self.game_won = True
        elif any(set(combination).issubset(set(self.pos_o)) for combination in [r1, r2, r3, c1, c2, c3, d1, d2]):
            self.game_won = True
        else:
            self.game_won = False
    
    def win_pos(self):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]              # Diagonals
        ]

        for combination in winning_combinations:
            if all(pos in self.pos_x for pos in combination):
                return combination[0], combination[2], 'X'
            elif all(pos in self.pos_o for pos in combination):
                return combination[0], combination[2], 'O'
        
        return None

    def win(self):
        edge_correction_sx = SQUARE_SIZE / 2
        edge_correction_bx = SQUARE_SIZE / 2
        edge_correction_sy = SQUARE_SIZE / 2
        edge_correction_by = SQUARE_SIZE / 2
        start, end, player = self.win_pos()
        top_x = (start - 1) % 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        top_y = (start - 1) // 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        end_x = (end - 1) % 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        end_y = (end - 1) // 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        if start == 1 and end == 9:
            edge_correction_sx = - edge_correction_sx
            edge_correction_sy = - edge_correction_sy
        elif start == 3 and end == 7:
            edge_correction_bx = - edge_correction_bx
            edge_correction_sy = - edge_correction_sy
        elif start in [1,4,7] and end in [3,6,9]:
            edge_correction_sy = 0
            edge_correction_by = 0
            edge_correction_sx = - edge_correction_sx
        elif start in [1,2,3] and end in [7,8,9]:
            edge_correction_sx = 0
            edge_correction_bx = 0
            edge_correction_sy = - edge_correction_sy
        self.canvas.create_line(top_x + edge_correction_sx, top_y + edge_correction_sy, end_x + edge_correction_bx, end_y + edge_correction_by, fill=self.win_line, width=7)
        self.canvas.unbind('<Button-1>')
        self.game_over(player)

    def game_over(self,player):
            self.canvas.create_text(SQUARE_SIZE * 1.5, SQUARE_SIZE,
                            text=f'Game over {player} \n  wins!',
                            font=('Terminal', TEXT_SIZE),
                            fill=self.txt_color
                           )

    def draw(self):
            self.canvas.create_text(SQUARE_SIZE * 1.5, SQUARE_SIZE,
                            text=f' Game over XO\n  draw!',
                            font=('Terminal', TEXT_SIZE),
                            fill=self.txt_color
                           )
            
    def reset(self, event=None):
        self.canvas.delete('all')
        self.play_grid()

        self.x = None
        self.y = None
        self.turn = 0
        self.AI_turns = 1

        self.pos_x = []
        self.pos_o = []
        self.pos_o_over_flow = []
        self.objs_x = []
        self.objs_o = []
        self.empty_pos = [1,2,3,4,5,6,7,8,9]

        self.game_won = False
        self.canvas.bind('<Button-1>', self.input_sqare)
        

    def play_grid(self):
        for i in range (1, 3):
            self.canvas.create_line(SQUARE_SIZE * i,
                                0,
                                SQUARE_SIZE * i,
                                CANVAS_SIZE,
                                width= 5,
                                fill=self.grid
                                )
        for j in range (1, 3):
            self.canvas.create_line( 0,
                                SQUARE_SIZE * j,
                                CANVAS_SIZE,
                                SQUARE_SIZE * j,
                                width= 5,
                                fill=self.grid
                                )
            
    def cross(self, col, row):
        top_x = col * SQUARE_SIZE
        top_y = row * SQUARE_SIZE
        pos = row * 3 + col + 1
        if pos not in self.pos_x and pos not in self.pos_o or self.redraw:
            obj = self.canvas.create_line(top_x + IN_BOARDER,
                            top_y + IN_BOARDER,
                            top_x + SQUARE_SIZE - IN_BOARDER,
                            top_y + SQUARE_SIZE - IN_BOARDER,
                            fill= self.x_color,
                            width= 5
            )
            obj2 = self.canvas.create_line(top_x + SQUARE_SIZE - IN_BOARDER,
                            top_y + IN_BOARDER,
                            top_x + IN_BOARDER,
                            top_y + SQUARE_SIZE - IN_BOARDER,
                            fill= self.x_color,
                            width= 5
            )
            if not self.redraw:
                self.pos_x.append(pos)
                self.board_state()
                self.objs_x.append(obj)
                self.objs_x.append(obj2)
                if len(self.pos_o) + len(self.pos_x) > self.peices_allowed and not self.normal_game_mode:
                    self.empty_pos.append(self.pos_x[0])
                    del self.pos_x[0]
                    for i in range(2):
                        move_to_delete = str(self.objs_x[0])
                        del self.objs_x[0]
                        self.canvas.delete(move_to_delete)

        else:
            self.turn -= 1

    def circle(self, col, row):
        top_x = col * SQUARE_SIZE
        top_y = row * SQUARE_SIZE
        pos = row * 3 + col + 1
        if pos not in self.pos_x and pos not in self.pos_o or self.redraw:
            obj = self.canvas.create_oval(top_x + IN_BOARDER,
                            top_y + IN_BOARDER,
                            top_x + SQUARE_SIZE - IN_BOARDER,
                            top_y + SQUARE_SIZE - IN_BOARDER,
                            fill= self.o_color,
                            width= 0
            )
            obj2 = self.canvas.create_oval(top_x + IN_BOARDER * 1.5,
                            top_y + IN_BOARDER * 1.5,
                            top_x + SQUARE_SIZE - IN_BOARDER * 1.5,
                            top_y + SQUARE_SIZE - IN_BOARDER * 1.5,
                            fill= self.o_in_fill,
                            width= 0
            )
            if not self.redraw:
                self.pos_o.append(pos)
                self.board_state()
                self.objs_o.append(obj)
                self.objs_o.append(obj2)
                if len(self.pos_o) + len(self.pos_x) > self.peices_allowed and not self.normal_game_mode:
                    self.empty_pos.append(self.pos_o[0])
                    del self.pos_o[0]
                    for i in range(2):
                        move_to_delete = str(self.objs_o[0])
                        del self.objs_o[0]
                        self.canvas.delete(move_to_delete)
        else:
            self.turn -= 1

    def rnd(self):
        empty_sqares = self.empty_pos
        idx = random.randrange(0, len(empty_sqares))

        return empty_sqares[idx]

    def eval(self):
        move = self.rnd()
        x = (move - 1) % 3
        y = (move - 1) // 3
        return x, y

def main():
    root = tk.Tk()  # Create the main window
    root.title('Tic Tak Toe')
    game = ttoLogic(root)
    root.mainloop()

main()