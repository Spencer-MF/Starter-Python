class dosethiswork():

    def __init__(s):
        s.lst = []

    def factorial(s,n):
        x = 1
        for i in range(1, n+1):
            x*=i
            s.lst.append(x)
    
    def printlst(s):
        print(s.lst)

    def control_flow(s):
        n = int(input('what intager would you like to factorial?\n'))
        s.factorial(n)
        s.printlst()

dw = dosethiswork()

def main():
    dw.control_flow()

main()