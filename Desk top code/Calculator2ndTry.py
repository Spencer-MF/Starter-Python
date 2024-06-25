import math
from niceToHaves import restartCode

def main():
    restart = restartCode(False)
    while(restart == True):
        force_restart = False
        operation = int(input("select an operation to perform: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Divide with remainder\n6. Exponential\n7. N root\n8. Log base\n"))
        if operation in [1,2,3,4,5,6,7,8]:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))

            if operation == 1:
                anws = addition(num1, num2)
                print('The awnser is ' + str(anws))
            elif operation == 2:
                anws = subtraction(num1, num2)
                print('The awnser is ' + str(anws))
            elif operation == 3:
                anws = multiplication(num1, num2)
                print('The awnser is ' + str(anws))
            elif operation == 4:
                anws = division(num1, num2)
                print('The awnser is ' + str(anws))
            elif operation == 5:
                whole, remain = division_r(num1, num2)
                print('The awnser is ' + str(whole) + ' with a remainder of ' + str(remain))
            elif operation == 6:
                anws = exponet(num1, num2)
                print('The awnser is ' + str(anws))
            elif operation == 7:
                anws = nth_root(num1, num2)
                print('The awnser is ' + str(anws))
            elif operation == 8:
                anws = log_base(num1, num2)
                print('The awnser is ' + str(anws))
        else:
            print('Invalid input please try again')
            force_restart = True
        if force_restart != True:
            restart = restartCode(True)
        else:
            pass


def addition(num1, num2):
    awns = num1 + num2
    return awns

def subtraction(num1, num2):
    awns = num1 + num2
    return awns

def multiplication(num1, num2):
    awns = num1 * num2
    return awns

def division_r(num1, num2):
    awns_whole = num1 // num2
    awns_r = num1 % num2
    return int(awns_whole), int(awns_r)

def division(num1, num2):
    awns = num1 / num2
    return awns

def exponet(num1, num2):
    awns = num1 ** num2
    return awns

def nth_root(num1, root):
    awns = num1**(1/root)
    return awns

def log_base(num1, base):
    awns = math.log(num1, base)
    return awns

main()
