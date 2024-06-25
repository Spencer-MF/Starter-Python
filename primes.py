from Nicetohaves import Utility

class Primes():

    def isPrime(n):
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

