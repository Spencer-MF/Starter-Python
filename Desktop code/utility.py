class Utility():
            
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
                return st[num]