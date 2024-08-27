from utility import Utility

class Primes():

    def isPrime(self, n):
        if n <= 1:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True
    
    def set_of_all_prime(n):
        sieve = set(range(2, n+1))
        while sieve:
            prime = min(sieve)
            print(prime, end="\t")
            sieve -= set(range(prime, n+1, prime))
        return prime

    def all_primes_lower(value):
        progress = 0
        counter = 0
        for i in range(value):
            progress += 1
            if Primes.isPrime(i):
                end = Utility.end_of_num(i-1)
                counter += 1
                print(f'{i} is the {counter}{end} prime number under {value},   {progress}/{value}')

    def closestPrime(value):
        counter = 0
        i = 0
        allPrimes = []
        if Primes.isPrime(value):
            return value, None, None
        else:
            for i in range(value):
                if Primes.isPrime(i):
                    counter += 1
                    allPrimes.append(i)
            allPrimes.append(Primes.nth_prime(counter + 1, False, False))
            return None, allPrimes[counter], allPrimes[counter - 1]

    def nth_prime(count, Print, countUp):
        progress = 0
        counter = 0
        i = 0
        while(progress <  count):
            i += 1
            if Primes.isPrime(i):
                end = Utility.end_of_num(counter)
                counter += 1
                progress += 1
                if countUp and Print:
                    print(f'{i} is the {counter}{end} prime')
        if not countUp and Print:
            print(f'{i} is the {counter}{end} prime')
        return i
    
    def closestPrimeOut():
        value = int(input('What value would you like to find the closest prime numbers to? '))
        in_is_prime, higher_prime, lower_prime = Primes.closestPrime(value)
        if in_is_prime != None:
            print(f'{in_is_prime} is prime')
        else:
            print(f'{higher_prime} is the closest prime more than {value}')
            print(f'{lower_prime} is the closest prime less than {value}')

    def nth_prime_out():
        countUp = False
        value = int(input('What is the nth prime number you would like to find? '))
        countComf = input('Would you like all primes below requested prime? ')
        if countComf in ['y', 'Y', 'yes', 'Yes']:
            countUp = True
        Primes.nth_prime(value, True, countUp)

    def primes_list(value):
        nums = range(1, int(value))
        primes = list(filter(Primes.isPrime, nums))
        return primes
    
class Distropution():

    def __init__(self, pr):
        self.pr = pr
        self.max_prime_value = 0
        self.LD1 = []
        self.LD2 = []
        self.LD3 = []
        self.LD5 = []
        self.LD7 = []
        self.LD9 = []
        self.LDdict = {1:self.LD1, 2:self.LD2, 3:self.LD3, 5:self.LD5, 7:self.LD7, 9:self.LD9}

    def order(self):
        self.prime_sorter()
        self.dist_calc()

    def prime_sorter(self):
        n = self.max_prime_value
        for i in range(1, n+1):
            if pr.isPrime(i):
                self.prime_LD(i)

    def prime_LD(self, prime):
        LD = prime % 10
        lst = self.LDdict[LD]
        lst.append(prime)
        
    def dist_calc(self):
        LD1 = len(self.LD1)
        LD2 = len(self.LD2) 
        LD3 = len(self.LD3) 
        LD5 = len(self.LD5)
        LD7 = len(self.LD7)
        LD9 = len(self.LD9)
        total_primes = LD1 + LD2 + LD3 + LD5 + LD7 + LD9
        ends_in_1 = LD1 / total_primes * 100
        ends_in_2 = LD2 / total_primes * 100
        ends_in_3 = LD3 / total_primes * 100
        ends_in_5 = LD5 / total_primes * 100
        ends_in_7 = LD7 / total_primes * 100
        ends_in_9 = LD9 / total_primes * 100
        print(f'1: {ends_in_1}% {LD1}/{total_primes}\n')
        print(f'2: {ends_in_2}% {LD2}/{total_primes}\n')
        print(f'3: {ends_in_3}% {LD3}/{total_primes}\n')
        print(f'5: {ends_in_5}% {LD5}/{total_primes}\n')
        print(f'7: {ends_in_7}% {LD7}/{total_primes}\n')
        print(f'9: {ends_in_9}% {LD9}/{total_primes}\n')


class DistroV2():

    def __init__(self, pr, di):
        self.pr = pr
        self.di = di
        self.n = 10
        self.total = 0
        self.LDdict = {}
        self.LDratio = {}

    def order(self):
        self.LDdictSetUp()
        self.prime_sort()
        self.calc()
        self.display()

    def LDdictSetUp(self):
        for i in range(self.n):
            self.LDdict[i] = 0

    def prime_sort(self):
        n = di.max_prime_value
        for i in range(1, n+1):
            if pr.isPrime(i):
                self.prime_LD(i)
                self.total += 1
    
    def prime_LD(self, prime):
        LD = prime % self.n
        self.LDdict[LD] += 1

    def calc(self):
        for key in self.LDdict.keys():
            self.LDratio[key] = self.LDdict[key] / self.total * 100

    def display(self):
        for key in self.LDratio.keys():
            if self.LDratio[key] > 1:
                print(f'{key}: {self.LDratio[key]}% {self.LDdict[key]}/{self.total}\n')
            
class Controls():

    
    def __init__(self, di, di2):
        self.di = di
        self.di2 = di2

    def verstion_con(self):
        while True:
            ver = input('what vertion vertion of prime sorter do you want?\n1. First Edition\n2. Second Edition\n')
            if ver in ['1', '1.', 'FE', 'fe', 'Fe', 'First edition', 'first edition', 'First Edition']:
                self.max_value_v1()
                break
            elif ver in ['2', '2.', 'SE', 'se', 'Se', 'Second edition', 'second edition', 'Second Edition']:
                self.max_value_v2()
                break
            else:
                print("Invalid input try again")
    
    def max_value_v1(self):
        n = int(input('What is the upper bound of the primes you want the distrobution of?\n'))
        di.max_prime_value = n
        di.order()

    def max_value_v2(self):
        n = int(input('What is the upper bound of the primes you want the distrobution of?\n'))
        di.max_prime_value = n
        di2.order()
        

pr = Primes()
di = Distropution(pr)
di2 = DistroV2(pr, di)
con = Controls(di, di2)

def main():
    con.verstion_con()

Utility.restartCode(main)