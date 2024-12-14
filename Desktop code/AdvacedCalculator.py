import tkinter as tk

CANVAS_SIZE = 1200
BUTTON_SIZE_X = CANVAS_SIZE // 4
BUTTON_SIZE_Y = CANVAS_SIZE // 5
TEXT_SIZE = 200

class calculator_back_end:

    def __init__(self, root):
        self.x = None
        self.y = None

        self.number_digit = []
        self.cur_number = None
        self.all_numbers = []

        self.opperation_list = ['+', '-', 'x', '/']
        self.opperation = None
        self.all_opperations = []

        self.bg = 'white' 
        self.sybmol_color = 'black'
        self.grid = 'black'

        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, background=self.bg)    # makes that the window
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.keypad_input)

        self.display()

    def logic_controler(self):
        if self.opperation == None:
            self.input_decoder()
        else:
            self.store_number()

    def keypad_input(self, event):
        self.x = event.x // BUTTON_SIZE_X
        self.y = event.y // BUTTON_SIZE_Y
        self.logic_controler()

    def input_decoder(self):
        number = 3*(self.y-1)+self.x+1
        n = number - 10
        if self.x == 1 and self.y == 4:
            self.number_digit.append(0) 
        elif self.x == 0 and self.y == 4:
            self.number_digit.append('.')
        elif self.x == 3:
            self.opperation = self.opperation_list[self.y-1]
        elif n < 0 :
            self.number_digit.append(number)
        else:
            pass
        print(self.x, self.y)
        
    def store_number(self):
        n = self.digit_converter(self.number_digit)
        self.all_numbers.append(n)
        self.all_opperations.append(self.opperation)
        self.number_digit = []
        self.opperation = None
        print(self.all_numbers, self.all_opperations)

    def digit_converter(self, nums): 
        return float(''.join(str(i) for i in nums)) # Generator exp.

    def display(self):
        # these two for loops each raw two lines this first one is vertical and the second one is horizontal, it incroments them 1 and 2 square sizes so each square is the same size
        for i in range (1, 4):
            self.canvas.create_line(BUTTON_SIZE_X * i,
                                BUTTON_SIZE_Y,
                                BUTTON_SIZE_X * i,
                                CANVAS_SIZE,
                                width= 5,
                                fill=self.grid
                                )
        for j in range (1, 5):
            self.canvas.create_line( 0,
                                BUTTON_SIZE_Y * j,
                                CANVAS_SIZE,
                                BUTTON_SIZE_Y * j,
                                width= 5,
                                fill=self.grid
                                )
        for m in range (1, 4):
            for n in range (1, 4):
                self.canvas.create_text(BUTTON_SIZE_X * n - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * m  + BUTTON_SIZE_Y/2,
                                text= f'{3*(m-1)+n}',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 1 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 4  + BUTTON_SIZE_Y/2,
                                text= '.',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 2 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 4  + BUTTON_SIZE_Y/2,
                                text= '0',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 3 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 4  + BUTTON_SIZE_Y/2,
                                text= '=',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 1  + BUTTON_SIZE_Y/2,
                                text= '+',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 2  + BUTTON_SIZE_Y/2,
                                text= '-',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 3  + BUTTON_SIZE_Y/2,
                                text= 'x',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X/2,
                                BUTTON_SIZE_Y * 4  + BUTTON_SIZE_Y/2,
                                text= '/',
                                font=('Terminal', TEXT_SIZE),
                                fill=self.grid
                                )
        

def main():
    root = tk.Tk()                                                        # Create the main window
    root.title('Advanced Calculator')                                             # titles the window
    game = calculator_back_end(root)                                                 # runs the game
    root.mainloop()                                                       # makes keeps the game running untill closed manualy

# calls the function 
main()







