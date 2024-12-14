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
