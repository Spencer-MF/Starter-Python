import math
while(True):
    print("select an operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")
    print("6. N root")
    print("7. Log base")

    operation = input()

    if operation == "1": #add
        num1 = input("Enter addend: ")
        num2 = input("Enter second addend: ")
        print("The sum is " + str(int(num1) + int(num2)))
    elif operation == "2": #subtract
        num1 = input("Enter Minuend: ")
        num2 = input("Enter Subtrachend: ")
        print("The differemce is " + str(int(num1) - int(num2)))
    elif operation == "3": #multiply
        num1 = input("Enter Multiplicand: ")
        num2 = input("Enter Multiplier: ")
        print("The product is " + str(int(num1) * int(num2)))
    elif operation == "4": #divide
        num1 = input("Enter Dividend: ")
        num2 = input("Enter Divisor: ")
        print("The quotient is " + str(int(num1) / int(num2)))
    elif operation == "5": #exponential
        num1 = input("Enter base: ")
        num2 = input("Enter exponent: ")
        print("the power is " + str(int(num1)**int(num2)))
    elif operation == "6": #N root
        num1 = input("Enter Radicand: ")
        num2 = input("Enter index: ")
        print("the root is " + str(int(num1)**(1/int(num2))))
    elif operation == "7": #Log base
        num1 = input("Enter base: ")
        num2 = input("Enter agruemnt: ")
        print("the exponent is " + str(math.log(int(num2),int(num1))))
    else:
        print("invalid input")

    print("Would you like to perform another operation?")
    print("Yes  No")

    repeat = input()

    if repeat == "No":
        break
    elif repeat == "no":
        break
    elif repeat == "N":
        break
    elif repeat == "n":
        break
    elif repeat == "Yes":
        print("Ok")
    elif repeat == "yes":
        print("Ok")
    elif repeat == "Y":
        print("Ok")
    elif repeat == "y":
        print("Ok")
    else:
        print("Invalid input")
        break