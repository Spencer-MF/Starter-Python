import math

#n = input("what digit of the fibinachi squence would you like to know: ")
# explicitMethod = (((1+math.sqrt(5))**int(n))-((1-math.sqrt(5))**int(n)))/(2**int(n)*math.sqrt(5))

def FibinachiSq(value, list = False):
    counter = 0
    starterValue = 1
    holdValue = 0
    pastValue = 0
    n = value

    while(counter < int(n)): 
        starterValue = starterValue + holdValue
        holdValue = holdValue + pastValue
        pastValue = starterValue - holdValue
        if list == True:
            print(starterValue)
        counter += 1 
    
    print ('the value from code: ' + str(starterValue))


# print ('the formula method: ' + str(explicitMethod))
# print ('the value from code: ' + str(starterValue))

def FibFor(value, list = False):
    starterValue = 1
    holdValue = 0
    pastValue = 0
    n = value

    for i in range(int(n)):
        # fib sq 1 
        starterValue = starterValue + holdValue
        # fib sq 2
        holdValue = holdValue + pastValue
        # makeing the second value of fib sq 2 the correct value
        pastValue = starterValue - holdValue
        if list == True:
            print(starterValue)
    
    print ('the value from the for loop version of the code: ' + str(starterValue))

def count_to_n(n):
    x = 0
    for i in range(n):
        x += 1
        print(str(x))

given_n = input('number to count to: ')
count_to_n(int(given_n))

    