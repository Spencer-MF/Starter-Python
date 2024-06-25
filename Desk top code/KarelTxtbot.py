
from niceToHaves import restartCode

# constants, size of the play area 3 by 3 where this is the upper bound not included in play area
N_ROWS_PULS_1 = 4
N_COLS_PLUS_1 = 4

def main():
    print("Welcome to first person Karel! You're at row 1, column 1, facing East (facing column 3)")
    # start x and y positon
    curr_col = 1
    curr_row = 1
    # if facing in the x or y for incrmentaion when moveing in said direction
    facing_row = 0
    facing_col = 1
    # keeping track of the times turned so that the array that updates facing col, row, and direction. it is at one beacuse turn dosen't inc till after everything changes as all base var numbers are the starting pos
    times_turned = 1
    # to define facing direction and if player never turns left it need to have a known direction
    facing_direction = 'East.'
    # to contain the while loop
    has_finnished = False
    # so the move funtion dosen't print both posion and can't move
    not_moved = None
    while has_finnished == False:
        user_command = input('What would you like to do? You can move and turn left. Press enter to finish. ')
        if user_command == 'move':
            # calls move function and pass curr col, and curr row ro be incr and checks if moved, the facing var are to incr in the correct direction (+ or - curr pos) and facing direction is to incr the var (row or col)
            curr_col, curr_row, not_moved = move(curr_col, curr_row, facing_col, facing_row, facing_direction)
            if not_moved != True:
                print('You moved one step forward and now', "you're at row", curr_row, 'column ' + str(curr_col) + '.')
        elif user_command == 'turn left':
            # call turn left cycles through the values in the array for the incroment value (where row or col should be add to or sub from) for row and col (times turned checks what to update to)
            facing_col, facing_row, facing_direction, times_turned = turn_left(facing_col, facing_row, times_turned)
            print('You turned left and are now facing', facing_direction)
        elif user_command == '':
            # print the current state of play then ends the while loop
            print("You've ended up at row", curr_row, 'and column', curr_col, 'facing', facing_direction)
            has_finnished = True
        else:
            # allows for invalid inputs with out crashing the program
            print('Invalid command try something else ')

# moves the player in the 3 X 3 grid
def move(curr_col, curr_row, facing_col, facing_row, facing_direction):  
    # incr the the curr row and col (this is why 0 is in the row is it incr by nothing)
    # move test is to determin if the move is valid    
    move_test_col = curr_col + facing_col
    move_test_row = curr_row + facing_row
    # checks the direction of to dicide wether to incr cols or rows
    if facing_direction in ['East.', 'West.']:
        # tests if move is valid if it is test move overrides curr pos
        if 0 < move_test_col < N_COLS_PLUS_1:
            curr_col = move_test_col
            not_moved = False                       # used to confrim that play moved so it only prints the updated pos when a move happens
            return curr_col, curr_row, not_moved
        else:
            print("You can't move forward! ")
            not_moved = True                        # used to confirm that player has not moved to only print that the move didn't happen
            return curr_col, curr_row, not_moved
    else:                                           # same as the first part but from rows instead of cols
        if 0 < move_test_row < N_ROWS_PULS_1:
            curr_row = move_test_row
            not_moved = False
            return curr_col, curr_row, not_moved
        else:
            print("You can't move forward! ")
            not_moved = True
            return curr_col, curr_row, not_moved

# turn left changes the facing dirction and the incroment for rows and cols
def turn_left(facing_col, facing_row, times_turned):
    test_face_row = [0, 1, 0, -1]   # x comp   the these are the angle when you take the sin or cos for x and y (when faceing at 90 degress the x = cos(90) and the y = sin(90)) these are facing 0 deg, 90 deg, 180 deg, 270 deg, resptively
    test_face_col = [1, 0, -1, 0]   # y comp
    test_facing_direction = ['East.', 'North.', 'West.', 'South.'] # same as the last array just instead of cos and sin of the angle it names them
    facing_row = test_face_row[times_turned % 4]  
    facing_col = test_face_col[times_turned % 4]
    facing_direction = test_facing_direction[times_turned % 4]  # these three function take the times turn and devids them by the number of compents in the array (4) then takes the reaminder this is done so that if you turn 5 times you go back to the firt item in the array
    times_turned += 1                                           # incr times turned
    return facing_col, facing_row, facing_direction, times_turned

# There is no need to edit code beyond this point


restart = restartCode(False)
while(restart == True):
    main()
    restart = restartCode(True)