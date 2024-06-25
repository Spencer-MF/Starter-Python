def main():
    for i in range(101):
        if is_odd(i):
            print(i, 'odd')
        else:
            print(i, 'even')

def is_odd(n):
    odd_check = n % 2
    return odd_check == 1
    
main()