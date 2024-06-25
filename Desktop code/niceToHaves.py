
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
