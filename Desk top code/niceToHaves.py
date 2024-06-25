
def restartCode(Has_Run):
    if Has_Run is True: 
        continue_bool = True
        while(continue_bool == True):
                continue_question = input('Would you like to run this program again?\n')
                if continue_question in ['yes', 'Yes', 'y', 'Y', ' ']:
                    print('Restarting code')
                    continue_bool = True
                    break
                elif continue_question in ['no', 'No', 'n', 'N', '']:
                    print('Thank you for using this code')
                    continue_bool = False
                    break
                else:
                    print('invalid input try again')
        
        if continue_bool == True:
            return True
        else:
            return False
    else:
        return True