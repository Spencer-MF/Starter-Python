
import random
from niceToHaves import *

def main():
    print('this program averages two numbers')
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    ave = average(num1, num2)
    print('this is the average of those two numbers' + str(ave))


def average(num1, num2):
    ave = (num1 + num2)/2
    return ave

NUM_SIDES = 20

def die_roll():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    ave = average(die1, die2)
    print('You are rolling a D' + str(NUM_SIDES))
    print('The first die rolled a ' + str(die1))
    print('The second die rolled a ' + str(die2))
    print ('The average of the two die is ' + str(ave))


restart = restartCode(False)
while(restart == True):
    choice = input('would you like to try a diffrent number? \n')
    if choice in ['1', 'ave', 'average', '1.']:
        main()
                
    elif choice in ['2', '2.', 'dice', 'roll die', 'dice roll']:
        die_roll()
    else:
        print('invalid input try again')
    restart = restartCode(True)
