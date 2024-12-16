import tkinter as tk

CANVAS_SIZE = 1200
BUTTON_SIZE_X = CANVAS_SIZE // 4
BUTTON_SIZE_Y = CANVAS_SIZE // 5
TEXT_SIZE = CANVAS_SIZE // 6

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

        self.equals = False
        self.answer = None

        self.mode_list = [0, 1, 0, 1]
        self.mode = 0

        self.color_palette = ['white', 'black', 'blue', 'red']
        self.color_palette_inv = ['black', 'white', 'red', 'blue']
        self.theme = 0
        self.total_themes = len(self.color_palette)
        self.bg = self.color_palette[self.theme] 
        self.sybmol_color = self.color_palette_inv[self.theme]
        self.grid = self.color_palette_inv[self.theme]

        self.opperation_symbols = ['+', '−', '×', '÷']
        self.bottom_row_symbols = ['.', '0', '=']

        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, background=self.bg)    # makes that the window
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.keypad_input)
        root.bind('<Key-m>', self.mode_controller)
        root.bind('<Key-M>', self.mode_controller)
        root.bind('<Key-c>', self.clear_botton)
        root.bind('<Key-C>', self.clear_botton)
        root.bind('<Key-t>', self.themes)
        root.bind('<Key-T>', self.themes)

        self.display()
        self.mode_display()

    def logic_controler(self):
        self.input_decoder()
        if self.mode_list[self.mode] == 1:
            if self.equals:
                if self.answer == None:
                    self.store_number()
                    self.math_mode_1()
                self.equals = False
                self.answer = None
            elif len(self.all_numbers) == 2:
                self.math_mode_1()
        elif self.equals:
            self.store_number()
            self.math_mode_0()
            self.equals = False

    def keypad_input(self, event):
        self.x = event.x // BUTTON_SIZE_X
        self.y = event.y // BUTTON_SIZE_Y
        self.logic_controler()

    def input_decoder(self):
        number = 3*(self.y-1)+self.x+1
        n = number - 10
        if self.x == 1 and self.y == 4:
            self.number_digit.append(0)
            self.input_display() 
        elif self.y == 0:
            pass
        elif self.x == 0 and self.y == 4:
            self.number_digit.append('.')
        elif self.x == 3:
            self.opperation = self.opperation_list[self.y-1]
            self.store_operation()
            if len(self.number_digit) > 0:
                self.store_number()
            print(self.all_numbers)
        elif n < 0 :
            self.number_digit.append(number)
            self.input_display()
        else:
            self.equals = True         
        
    def store_number(self):
        n = self.digit_converter(self.number_digit)
        self.all_numbers.append(n)
        self.number_digit = []
        self.opperation = None
    
    def store_operation(self):
        if self.opperation != None:
            self.all_opperations.append(self.opperation)

    def digit_converter(self, nums): 
        return float(''.join(str(i) for i in nums)) # Generator exp.
    
    def digit_converter_int(self, nums): 
        return int(''.join(str(i) for i in nums)) # Generator exp.

    def in_series_math(self):
        if self.all_opperations[0] == '+':
            self.answer = self.all_numbers[0] + self.all_numbers[1]
        elif  self.all_opperations[0] == '-':
            self.answer = self.all_numbers[0] - self.all_numbers[1]
        elif self.all_opperations[0] == 'x':
            self.answer = self.all_numbers[0] * self.all_numbers[1]
        elif self.all_opperations[0] == '/':
            self.answer = self.all_numbers[0] / self.all_numbers[1]

    def math_mode_0(self):
        print(self.all_numbers)
        self.in_series_math()
        self.all_numbers.clear()
        self.all_opperations.clear()
        print(self.answer)
        self.answer_display()
    
    def math_mode_1(self):
        print(self.all_numbers, self.all_opperations)
        self.in_series_math()
        self.all_opperations.pop(0)
        self.all_numbers.clear()
        self.all_numbers.append(self.answer)
        self.answer_display()
        print(self.all_numbers, self.all_opperations)

    def mode_controller(self, event=None):
        self.mode = (self.mode + 1) % len(self.mode_list)
        self.update_screen()
        self.clear_all_data()
    
    def themes(self, event=None):
        self.theme = (self.theme + 1) % self.total_themes
        self.bg = self.color_palette[self.theme]
        self.sybmol_color = self.color_palette_inv[self.theme]
        self.grid = self.color_palette_inv[self.theme]
        self.reset_screen()

    def answer_display(self):
        if self.answer % 1 == 0:
            self.answer = int(self.answer)
        else:
            self.answer = round(self.answer, 2)
        self.update_screen()
        ans = self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X,
                            BUTTON_SIZE_Y * 0  + BUTTON_SIZE_Y/2,
                            text= f'{self.answer}',
                            font=('Terminal', TEXT_SIZE),
                            fill=self.grid
                            )
    
    def input_display(self):
        self.update_screen()
        if '.' in self.number_digit:
            n = self.digit_converter(self.number_digit)
        else:
            n = self.digit_converter_int(self.number_digit)
        self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X,
                            BUTTON_SIZE_Y * 0  + BUTTON_SIZE_Y/2,
                            text= f'{n}',
                            font=('Terminal', TEXT_SIZE),
                            fill=self.grid
                            )
    
    def clear_botton(self, event=None):
        self.clear_all_data()
        self.update_screen()

    def clear_all_data(self):
        self.all_numbers.clear()
        self.all_opperations.clear()
        self.answer = None
        self.number_digit.clear()

    def update_screen(self):
        self.canvas.delete('all')
        self.display()
        self.mode_display()
    
    def reset_screen(self):
        self.canvas.config(bg=self.bg)
        self.update_screen()
        self.canvas.update_idletasks()
    
    def mode_display(self):
        self.canvas.create_text(BUTTON_SIZE_X // 4,
                            BUTTON_SIZE_Y // 4,
                            text= f'{self.mode_list[self.mode]}',
                            font=('Terminal', TEXT_SIZE//5),
                            fill=self.grid
                            )


    def display(self):
        # these two for loops each raw three and four lines this first one is vertical and the second one is horizontal, it incroments them in sets square sizes so each square is the same size
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
                
        for x in range(1, 4):
            self.canvas.create_text(BUTTON_SIZE_X * x - BUTTON_SIZE_X/2,
                                    BUTTON_SIZE_Y * 4  + BUTTON_SIZE_Y/2,
                                    text= self.bottom_row_symbols[x - 1],
                                    font=('Terminal', TEXT_SIZE),
                                    fill=self.grid
                                    )
        for y in range(1, 5):
            self.canvas.create_text(BUTTON_SIZE_X * 4 - BUTTON_SIZE_X/2,
                                    BUTTON_SIZE_Y * y  + BUTTON_SIZE_Y/2,
                                    text= self.opperation_symbols[y - 1],
                                    font=('Terminal', TEXT_SIZE),
                                   fill=self.grid
                                    )


def main():
    root = tk.Tk()                                                        # Create the main window
    root.title('Advanced Calculator')                                             # titles the window
    game = calculator_back_end(root)                                                 # runs the calculator
    root.mainloop()                                                       # makes keeps the calculator running untill closed manualy

# calls the function 
main()
