import tkinter as tk
import random
import time

CANVAS_SIZE = 750                   # side langth of the window 
SQUARE_SIZE = CANVAS_SIZE // 3      # the size of the inner squars of the board
IN_BOARDER = 10                     # makes the x's and o's have a bit of space between them and the grid
TEXT_SIZE = CANVAS_SIZE // 11       # size of the end text
AI_THINK_TIME = 0.2                 # used to deley the ai move so its not instant (the unit is in seconds)


class ttoLogic:

    def __init__(self, root):
        self.x = None           # the col position used both to track where the mouse clicked and to place the x or o in the correct place
        self.y = None           # the row '                                                                                               '
        self.turn = 0           # tracks the turns, even turns are x and odd thurns are o

        self.objs_x = []        # list of the x shape names used in the alternate game mode where after 7(or what ever self.peices_allowed equals) moves are made the first one is deleted
        self.objs_o = []        # same as above but for o


        self.pos_x = []         # list of places x when in the form of numbers between 1 and 9 and not row col cords
        self.pos_o = []         # same but for o
        self.empty_pos = [1,2,3,4,5,6,7,8,9]  # list of empty position when a move it made the corsipoding number is removed

        self.theme = 0          # what the colors of the game look like (currently only two but it is a number so if I want to add more i don't have to remake it)

        # defalt colors
        self.bg = 'white' 
        self.grid = 'black'
        self.x_color = 'red'
        self.o_color = 'blue'
        self.o_in_fill = self.bg   # needs to be the same to make it look like a ring and not a filled circle
        self.txt_color = self.grid # could be any color but if bg is white or black its easy to have it just be the opposit of the bg 
        self.win_line = 'lime'     # the line that shows the winning move

        self.redraw = False        # used to update the o_in_fill and txt when the theme is changed

        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, background=self.bg)    # makes that the window
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.input_sqare)  # when user right click's self.input_sqare is run
        root.bind('<Key-r>', self.reset)        # when the the letter (case sensitve) after Key- is pressed corisponding function is run
        root.bind('<Key-R>', self.reset)
        root.bind('<Key-a>', self.play_AI)
        root.bind('<Key-A>', self.play_AI)
        root.bind('<Key-m>', self.mode)
        root.bind('<Key-M>', self.mode)
        root.bind('<Key-t>', self.themes)
        root.bind('<Key-T>', self.themes)

        self.playing_AI = False           # if player v player or player v ai
        self.game_mode = 0                # same as self.theme controls game mode (only two for now but if i want to add more i don't have to add more logic)
        self.normal_game_mode = True      # the bool verstion of self.game_mode
        self.peices_allowed = 7           # amount of peices allowed but for they get deleted in the alt game mode
        self.AI_turns = 1                 # used to track when its not the ai's turn to call turns_pve again so you don't have to click on the screen to have the ai play its move

        self.game()                       # draws the grid for the game         
        self.turns_pvp()                  # dosen't do anything here but its the function for pass play
        self.turns_pve()                  # dosen't do anything here but its the function for player vs computer (random move)
        self.game_won = False             # sets the bool that checks if the game has been won to false

    # this function is called by clicking on the screen and sets the game logic to run, there is no while loop for this game
    def input_sqare(self, event):
        self.x = event.x // SQUARE_SIZE
        self.y = event.y // SQUARE_SIZE

        # choses witch turn function to call based on if the player wants to play agains the another player or the computer
        if not self.playing_AI:
            self.turns_pvp() # player vs player
        else:
            self.turns_pve() # player vs computer

    # if a or A is pressed it will togle between player vs player or player vs computer
    def play_AI(self, event=None):
        if self.playing_AI:
            self.playing_AI = False
        else:
            self.playing_AI = True
    
    # if m or M is pressed it will togle between game modes, normal or the alternate, it was writen this way to allow for easy implementation of more than two game modes
    def mode(self, event=None):
        if self.game_mode == 0:
            self.game_mode = 1
            self.normal_game_mode = False
        else:
            self.game_mode = 0
            self.normal_game_mode = True
    
    # if t or T is pressed it will togle between color schemes (right now its only a light and dark mode) coded this way to allow for more colors schemes to be added easly
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
        
        # when the theme is changed all shapes get deleted and then redrawn with the new colors
        self.canvas.delete('all')
        if len(self.pos_o) > 0:                 # redraws all moves in the same place but with new colors
            self.redraw = True
            for i in range(len(self.pos_o)):
                rc = self.pos_o[i]              # used to change a single number 1-9 into two numbers row col (1,1) 
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
        self.redraw = False                     # cancels redraw to end the altrnate logic only used here

        if self.game_won:                       # if the game has was won this will redraw the text in the new colors
            self.win()
        
        # redraws the background of the window and the grid as these are only drawn when the game is started
        self.canvas.config(bg=self.bg)
        self.play_grid()
        self.canvas.update_idletasks()

    # this is the logic for the player vs player turn
    def turns_pvp(self):
        # this is to make sure a number is actually passed through 
        if self.x is not None and self.y is not None:
            whos_turn = self.turn                       # this has to be stored in a temp var to tell if the turn is odd or even
            whos_turn %= 2
            if whos_turn == 0:                          # if the turn is even it the x turn
                self.turn += 1                          # incroments the turn count
                self.cross(self.x, self.y)
            else:                                       # if the turn is odd it the o turn, this is an else as it can only be odd or even
                self.turn += 1                         
                self.circle(self.x, self.y)             
        self.game_win()                                 # calls the function that checks if the game has been won if the game has been won self.game_won will be set to Turn other wise it will be set to False
        if self.game_won:
            self.win()                                  # calls the function the draws the line the goes through the three in a row
        elif len(self.empty_pos) == 0:                  # if there are no more places to play the game is a tie, orginaly this was if self.turn equal to 9 but in the alt game mode there can be more than 9 turns
            self.draw()                                 # calls the function that writes the text that the game is a tie

    # this is the logic for the player vs computer turn, most of the logic is the same as turns_pvp
    def turns_pve(self):
        if self.x is not None and self.y is not None:   # form here_______________
            whos_turn = self.turn
            whos_turn %= 2
            if whos_turn == 0:
                self.turn += 1
                self.cross(self.x, self.y)              # to here ________________ the code is the same
                self.AI_turns += 1                      # thus us counts that is not the ai turn 
            else:
                self.turn += 1
                self.canvas.update_idletasks()          # updates the screen so that the x is placed
                time.sleep(AI_THINK_TIME)               # delays the ai so it dosen't place its move intantly
                x, y = self.eval()                      # calls the computer to make its choice of the move it wants to make (currently just a random legal move)
                self.circle(x, y)
        self.game_win()                                 # same logic as turns_pvp
        if self.game_won:
            self.win()
        elif len(self.empty_pos) == 0:
            self.draw()
        elif self.AI_turns % 2 == 0:                    # this is used to call this function again when its the ai's turn so the player dosen't have click the srcreen for the computer to move
            self.turns_pve()                            # this function is run angain 

    # this function takes the moves made by x and o and removes them from empty_pos
    def board_state(self):
        used_pos = (self.pos_o + self.pos_x)            # joins the x and o move list
        for num in used_pos:                            # for all moves made it will remove all corisponding numbers 1-9 version
            if num in self.empty_pos:
                self.empty_pos.remove(num)

    # draws the grid, IDK why this is even a function it just calls another function that could be called with out this function. 
    # (the real resaon its here is because before i figured out i could use a class, i though i was going to have to pass canvas 
    # indivualy to each function so this function was made to make that easyer but once i found out you don't have to do that this 
    # became obsolite but i never bothered to fix it and will continue to not bother)
    def game(self):
        self.play_grid()

    # the function checks if x or o have won the game
    def game_win(self):

        # these are all the possible win states
        r1 = [1,2,3]        #
        r2 = [4,5,6]        #       1 | 2 | 3
        r3 = [7,8,9]        #       --+---+--
        c1 = [1,4,7]        #       4 | 5 | 6    
        c2 = [2,5,8]        #       --+---+--
        c3 = [3,6,9]        #       7 | 8 | 9 
        d1 = [1,5,9]        #
        d2 = [3,5,7]        # this is what the numbers represent 

        if any(set(combination).issubset(set(self.pos_x)) for combination in [r1, r2, r3, c1, c2, c3, d1, d2]):     # this checks if the places x have gone contage any one of the win states
            self.game_won = True
        elif any(set(combination).issubset(set(self.pos_o)) for combination in [r1, r2, r3, c1, c2, c3, d1, d2]):   # this checks if the places o have gone contage any one of the win states
            self.game_won = True
        else:                                                                                                       # if no one has won it sets game_won to False, this could also do nothing as it is set to false by defalt, it was just a releic from when it return true or false
            self.game_won = False
    
    # this function determins who won and how the the won, this probly could have been combined the the above function i just didn't feel like it
    def win_pos(self):

        # same combinations as the function before
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]              # Diagonals
        ]

        for combination in winning_combinations:                        # winning_combinations is a list of lists so for each list in the list is runs the loop, (so 8 times)
            if all(pos in self.pos_x for pos in combination):           # checks if x has all of the right pos to win (pos are the the squares that you could go) 
                return combination[0], combination[2], 'X'              # returns the start of the winning line the end of the winning line and the player the won
            elif all(pos in self.pos_o for pos in combination):         # same as above but for o insted of x
                return combination[0], combination[2], 'O'
        
        return None                                                     # if this function is called and no one won it gives bac nothing

    # this function draws the line that goes thorugh the winning move, now you see why i spent the time to write all of these notes, i have to many function with win or won in the name its getting hard to keep track and im too lazy to rename any of the function or variables
    def win(self):
        edge_correction_sx = SQUARE_SIZE / 2                            # with the way the code orginaly worked it would draw a line to the senter of the tile that won on the start and end side, this corrects for that
        edge_correction_bx = SQUARE_SIZE / 2                            # sx means start x and bx means bottom x same for sy and by but its the y componet insted
        edge_correction_sy = SQUARE_SIZE / 2
        edge_correction_by = SQUARE_SIZE / 2
        start, end, player = self.win_pos()                             # this call a function that return who won into the player var, and the atart square and the end square into start and end respectively
        top_x = (start - 1) % 3 * SQUARE_SIZE + SQUARE_SIZE / 2         # these function turn the start and end numbers that are 1-9 into rows and cols that are (0,0) to (2,2) 
        top_y = (start - 1) // 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        end_x = (end - 1) % 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        end_y = (end - 1) // 3 * SQUARE_SIZE + SQUARE_SIZE / 2
        if start == 1 and end == 9:                                     # corrects for the first diagnal, the diaginals have to checked first as other wise either the horizantal or virtical check would be go thorugh as true and then give the wronge corrections
            edge_correction_sx = - edge_correction_sx
            edge_correction_sy = - edge_correction_sy
        elif start == 3 and end == 7:                                   # corrects for the second diagnal
            edge_correction_bx = - edge_correction_bx
            edge_correction_sy = - edge_correction_sy
        elif start in [1,4,7] and end in [3,6,9]:                       # corrects for the horizantal wins
            edge_correction_sy = 0
            edge_correction_by = 0
            edge_correction_sx = - edge_correction_sx       
        elif start in [1,2,3] and end in [7,8,9]:                       # corrects of the virtical wins
            edge_correction_sx = 0
            edge_correction_bx = 0
            edge_correction_sy = - edge_correction_sy
        self.canvas.create_line(top_x + edge_correction_sx, top_y + edge_correction_sy, end_x + edge_correction_bx, end_y + edge_correction_by, fill=self.win_line, width=7)    # draws the line
        self.canvas.unbind('<Button-1>')                                # stops the input_square function form being called when the player right clicks on the screen
        self.game_over(player)                                          # call the function that draws the game over text, this is not the draw text witch gets called at the point that there are no moves left to make, the player is the var returned by win_pos

    # draws the text for who wins
    def game_over(self,player):
            self.canvas.create_text(SQUARE_SIZE * 1.5, SQUARE_SIZE,
                            text=f'Game over {player} \n  wins!',       # this it the player that won either displays X or O depending on who won
                            font=('Terminal', TEXT_SIZE),
                            fill=self.txt_color
                           )

    # draws the text if the game ends in a tie
    def draw(self):
            self.canvas.create_text(SQUARE_SIZE * 1.5, SQUARE_SIZE,
                            text=f' Game over XO\n  draw!',
                            font=('Terminal', TEXT_SIZE),
                            fill=self.txt_color
                           )
            
    # if r or R is pressed this function resests all the saved data to how it was when the game is first started with the expetion of the theme, if you are playing ai, and the game mode (ie normal or the alt version)
    def reset(self, event=None):
        self.canvas.delete('all')                                   # deletes all shapes drawn (includes text)
        self.play_grid()                                            # redraws the grid (see how this isn't self.game() that function is useless)

        # all the varibales between the these lines are reset to the same values given in the init function
        # ____________________________________________________________________
        self.x = None
        self.y = None
        self.turn = 0
        self.AI_turns = 1

        self.pos_x = []
        self.pos_o = []
        self.objs_x = []
        self.objs_o = []
        self.empty_pos = [1,2,3,4,5,6,7,8,9]

        self.game_won = False
        # ____________________________________________________________________
        self.canvas.bind('<Button-1>', self.input_sqare)            # re binds right click to run the input_square function, so that if the function is run after someone won a game you can play again    
        
    # draws the grid
    def play_grid(self):
        # these two for loops each raw two lines this first one is vertical and the second one is horizontal, it incroments them 1 and 2 square sizes so each square is the same size
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
            
    # draws the x's
    def cross(self, col, row):
        top_x = col * SQUARE_SIZE                                           # converts the order par (0,0) through (2,2) into the pixes at the top left corner of each square
        top_y = row * SQUARE_SIZE
        pos = row * 3 + col + 1                                             # turns the row and col into a number between 1 and 9
        if pos not in self.pos_x and pos not in self.pos_o or self.redraw:  # draws the \ part of the x
            obj = self.canvas.create_line(top_x + IN_BOARDER,
                            top_y + IN_BOARDER,
                            top_x + SQUARE_SIZE - IN_BOARDER,
                            top_y + SQUARE_SIZE - IN_BOARDER,
                            fill= self.x_color,
                            width= 5
           )
            obj2 = self.canvas.create_line(top_x + SQUARE_SIZE - IN_BOARDER, # draws the / part of the x
                            top_y + IN_BOARDER,
                            top_x + IN_BOARDER,
                            top_y + SQUARE_SIZE - IN_BOARDER,
                            fill= self.x_color,
                            width= 5
            )
            if not self.redraw:                                             # if the theme is changes a move wasn't made and the logic for the if a move was made is skiped
                self.pos_x.append(pos)                                      # add the move to list of moves that x has made in 1-9 form
                self.board_state()                                          # this delete said move for the list of available moves
                self.objs_x.append(obj)                                     # adds both \ and / shapes to a list 
                self.objs_x.append(obj2)
                if len(self.pos_o) + len(self.pos_x) > self.peices_allowed and not self.normal_game_mode:   # this the the logic for the alt game mode so if the alt game mode is selected and there have been more moves than allowed pieces (so the amout of x or o that can be on the board 7 at the moment)
                    self.empty_pos.append(self.pos_x[0])                    # adds the moved that about to be deleted back to the list of available moves
                    del self.pos_x[0]                                       # removed the move from x's moves (for both of these it will always be the first index as the move add first will be first and if that move it removed then the next move becomes first)
                    for i in range(2):                                      # has to run twice as the x is two shapes \ and /
                        move_to_delete = str(self.objs_x[0])                # this gets the id of the oldest shape and turns the number into a string
                        del self.objs_x[0]                                  # deletes the oldest id
                        self.canvas.delete(move_to_delete)                  # then deletes the actual shape this is run twice to get both haves but beacuse the obj that gets delited id also gets deleted it will always be the first index in the list

        # if an invalid move is made it skips all of the logic and undose the the turn
        else:
            self.turn -= 1

    # draws the o's the logic is completely identical the only diffrence is that insted of two shapes to form a x it a circle and then a smaller circle with the color of the backgrund to make it look like a ring 
    def circle(self, col, row):
        top_x = col * SQUARE_SIZE                                           # converts the order par (0,0) through (2,2) into the pixes at the top left corner of each square
        top_y = row * SQUARE_SIZE
        pos = row * 3 + col + 1                                             # turns the row and col into a number between 1 and 9
        if pos not in self.pos_x and pos not in self.pos_o or self.redraw:  # draws the ounter cercal part of the o
            obj = self.canvas.create_oval(top_x + IN_BOARDER,
                            top_y + IN_BOARDER,
                            top_x + SQUARE_SIZE - IN_BOARDER,
                            top_y + SQUARE_SIZE - IN_BOARDER,
                            fill= self.o_color,
                            width= 0
            )
            obj2 = self.canvas.create_oval(top_x + IN_BOARDER * 1.5,        # draws the inner punchout of the o the in boarder contant is pull dubble function as both the spaceing for the o as a whole but also to set the thickness of the ring, right now that is 5 px the same as the x, this could have been its own constant but I was too lazy
                            top_y + IN_BOARDER * 1.5,
                            top_x + SQUARE_SIZE - IN_BOARDER * 1.5,
                            top_y + SQUARE_SIZE - IN_BOARDER * 1.5,
                            fill= self.o_in_fill,
                            width= 0
            )
            if not self.redraw:                                             # if the theme is changes a move wasn't made and the logic for the if a move was made is skiped
                self.pos_o.append(pos)                                      # add the move to list of moves that o has made in 1-9 form
                self.board_state()                                          # this delete said move for the list of available moves
                self.objs_o.append(obj)                                     # add both the outer and inner circle to a list
                self.objs_o.append(obj2)
                if len(self.pos_o) + len(self.pos_x) > self.peices_allowed and not self.normal_game_mode:   # this the the logic for the alt game mode so if the alt game mode is selected and there have been more moves than allowed pieces (so the amout of x or o that can be on the board 7 at the moment)
                    self.empty_pos.append(self.pos_o[0])                    # adds the moved that about to be deleted back to the list of available moves
                    del self.pos_o[0]                                       # removed the move from o's moves (for both of these it will always be the first index as the move add first will be first and if that move it removed then the next move becomes first)
                    for i in range(2):                                      # has to run twice as the o is two shapes the outer one and the inner one
                        move_to_delete = str(self.objs_o[0])                # this gets the id of the oldest shape and turns the number into a string
                        del self.objs_o[0]                                  # deletes the oldest id
                        self.canvas.delete(move_to_delete)                  # then deletes the actual shape this is run twice to get both haves but beacuse the obj that gets delited id also gets deleted it will always be the first index in the list
        
        # if an invalid move is made it skips all of the logic and undose the the turn
        else:
            self.turn -= 1

    # this the logic behind the computer, and that is not logic at all just an random number generator
    def rnd(self):
        empty_sqares = self.empty_pos                                     # thid puts the list of avaible moves into another variable a totaly pointless thing to do come from when this was a diffenet class
        idx = random.randrange(0, len(empty_sqares))                      # generates a number from 0 to the amound to moves possible

        return empty_sqares[idx]                                          # uses that generated number to return the move that corresponds to the index of a move this is a number that is 1-9

    # this fucntion when called returns a row and a col and x and a y
    def eval(self):
        move = self.rnd()                                                 # generates a random legal move
        x = (move - 1) % 3                                                # turns that move that a number form 1-9 into a order pair form (0,0) to (2,2)
        y = (move - 1) // 3

        return x, y                                                       # returns that orderd pair
    
# this function is what runs the game
def main():
    root = tk.Tk()                                                        # Create the main window
    root.title('Tic Tak Toe')                                             # titles the window
    game = ttoLogic(root)                                                 # runs the game
    root.mainloop()                                                       # makes keeps the game running untill closed manualy

# calls the function 
main()