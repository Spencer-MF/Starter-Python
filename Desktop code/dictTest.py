class Dicttest():

    def __init__ (self):
        self.dict = {}
        self.binary_string = 0

    '''
    def how_many_0_or_1(self):
        binary = list(self.binary_string)
        for bit in binary:
            self.dict[bit] += 1 
        print(f'{self.dict['0']}')
        print(f'{self.dict['1']}')
    '''
    def hm0o1(self):
        self.dict[self.binary_string] += 1
        print(f'{self.dict[0]}')

    
    
dt = Dicttest()

def main():
    #dt.how_many_0_or_1()
    dt.hm0o1()

main()