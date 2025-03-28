import random

class Utility():

    def end_of_num(num):
        num_error = num % 100
        num %= 10
        st = ['st', 'nd', 'rd', 'th']
        if num_error in [11,12,13]:
            return st[3]
        else:
            if num > 3:
                return st[3]
            else:
                return st[num - 1]
            
    def restart(function_to_restart):
        n = ''
        while n == '':
            function_to_restart()
            n = input()

    def restartCode(Funtion_to_run): 
        Funtion_to_run()
        continue_bool = True
        while(continue_bool == True):
                continue_question = input('Would you like to run this program again?\n')
                if continue_question in ['yes', 'Yes', 'y', 'Y', '']:
                    print('Restarting code')
                    continue_bool = True
                    Funtion_to_run()
                elif continue_question in ['no', 'No', 'n', 'N', ' ']:
                    print('Thank you for using this code')
                    continue_bool = False
                    break
                else:
                    print('invalid input try again')

    def cool_code():
        i = random.random()
        j = random.random()
        n = i+j

        if n < 2.0:
            if n < 1.0:
                if n < 0.5:
                    if n < 0.25:
                        print('0-0.25')
                    else:
                        print('0.25-0.5')
                else:
                    if n > 0.75:
                        print('0.25-0.75')
                    else:
                        print('0.75-1')
            else:
                if n < 1.5:
                    if n < 1.25:
                        print('1-1.25')
                    else:
                        print('1.25-1.5')
                else:
                    if n > 1.75:
                        print('1.25-1.75')
                    else:
                        print('1.75-1')
        else:
            print('2-inf')

        print(n)

