from testingPython import Fibsq
from qudatic import Quadratic
from primes import Primes
from factorial import Factorial
from Nicetohaves import Utility

def main():
    print('what fomula would you like to use')
    print('1. qudatic equation solver')
    print('2. cross product solver')
    print('3. fibinachi squcence solver')
    print('4. closest value fibinachi solver')
    print('5. closest prime to your number')
    print('6. the nth prime')
    print('7. factoral of a given number')

    operation = input('input the number of the diared operation: ')


    if operation == '1':
        Quadratic.qudaticEq()
    elif operation == '2':
        print('sorry but this feture')
        print('still in development')
    elif operation == '3':
        Fibsq.fibniachi()
    elif operation == '4':
        Fibsq.altfib()
    elif operation == '5':
        Primes.closestPrimeOut()
    elif operation == '6':
        Primes.nth_prime_out()
    elif operation == '7':
        Factorial.n_fact_out()
    else:
        print('invalid input. try again')

Utility.restart(main)