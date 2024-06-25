from fibinachiSq import FibinachiSq, FibFor
from niceToHaves import restartCode

def main():
        restart = restartCode(False)
        while(restart == True):
            n = input("what digit of the fibinachi squence would you like to know: ")
            code_type = input('what verstion of the code would you like to run? \n1. while version \n2. for version \n')

            if code_type == str(1):
                FibinachiSq(n,False)
            elif code_type == str(2): 
                FibFor(n, False)
            else:
                print('invalid input')
            restart = restartCode(True)
            


main()