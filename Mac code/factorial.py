class Factorial():

    def n_factorial(value):
        hold = 1
        for i in range(1, value + 1):
            hold *= i
        return hold
    
    def n_fact_out():
        value = int(input('What number would you like to factorial? '))
        out = Factorial.n_factorial(value)
        print(f'{out} is the factorial of {value}')

