from Nicetohaves import Utility

def main():
    i = input('Would you like 1. to know if a number is odd or even or 2. all numbers to your number that are odd or even?\n')
    if i in ['1', '1.']:
        n = int(input('What number would you like to now if odd or even? '))
        odd = is_odd(n)
        if odd:
            print(n, 'is odd')
        else:
            print(n, 'is even')
    elif i in ['2', '2.']:
        upto()
        

def is_odd(n):
    odd_check = n % 2
    return odd_check == 1
    
def upto():
    n = int(input('to what number do you want to know the odds and even: '))
    for i in range(n + 1):
        if is_odd(i):
            print(i, 'odd')
        else:
            print(i, 'even')
    
Utility.restart(main)