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
        self.ld1 = []
        self.ld2 = []
        self.ld3 = []
        self.ld5 = []
        self.ld7 = []
        self.ld9 = []
        self.lddict = {1:self.ld1, 2:self.ld2, 3:self.ld3, 5:self.ld5, 7:self.ld7, 9:self.ld9}

    def prime_sorter(self):
        n = self.max_prime_value
        for i in range(1, n+1):
            if pr.isPrime(i):
                self.prime_ld(i)
        self.dist_calc()

    def prime_ld(self, prime):
        ld = prime % 10
        lst = self.lddict[ld]
        lst.append(prime)
        
    def dist_calc(self):
        ld1 = len(self.ld1)
        ld2 = len(self.ld2) 
        ld3 = len(self.ld3) 
        ld5 = len(self.ld5)
        ld7 = len(self.ld7)
        ld9 = len(self.ld9)
        total_primes = ld1 + ld2 + ld3 + ld5 + ld7 + ld9
        ends_in_1 = ld1 / total_primes * 100
        ends_in_2 = ld2 / total_primes * 100
        ends_in_3 = ld3 / total_primes * 100
        ends_in_5 = ld5 / total_primes * 100
        ends_in_7 = ld7 / total_primes * 100
        ends_in_9 = ld9 / total_primes * 100
        print(f'1: {ends_in_1}% {ld1}/{total_primes}\n')
        print(f'2: {ends_in_2}% {ld2}/{total_primes}\n')
        print(f'3: {ends_in_3}% {ld3}/{total_primes}\n')
        print(f'5: {ends_in_5}% {ld5}/{total_primes}\n')
        print(f'7: {ends_in_7}% {ld7}/{total_primes}\n')
        print(f'9: {ends_in_9}% {ld9}/{total_primes}\n')
        
        
class Controls():
    
    def __init__(self,di):
        self.di = di
    
    def max_value(self):
        n = int(input('What is the upper bound of the primes you want the distrobution of?\n'))
        di.max_prime_value = n
        di.prime_sorter()


pr = Primes()
di = Distropution(pr)
con = Controls(di)

def main():
    con.max_value()

Utility.restartCode(main)