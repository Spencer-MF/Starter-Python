
class Quadratic:

    def qudaticEq():
        inA = input('input the constants of your equation \na: ')
        inB = input('b: ')
        inC = input('c: ')
        a = int(inA)
        b = int(inB)
        c = int(inC)
        awns1 = (-b+(((b**2)-(4*(a)*(c)))**(1/2)))/(a*2)
        awns2 = (-b-(((b**2)-(4*(a)*(c)))**(1/2)))/(a*2)
        print(awns1)
        print(awns2)
