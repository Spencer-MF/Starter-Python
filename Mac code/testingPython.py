from Nicetohaves import Utility

class Fibsq:

    def fibniachi():
        countUp = False
        startValue = 1
        holdValue = 0
        pastValue = 0
        value = input('what value of the fibinachi sequence would you like to know? ')
        ifCountUp = input(f'would you like know all values up to {value}: ')
        if ifCountUp in ['y','Y','Yes','yes']:
            countUp = True
        else:
            countUp = False
        n = int(value)

        for i in range(n):
            startValue = startValue + holdValue
            holdValue = holdValue + pastValue
            pastValue = startValue - holdValue
            end = Utility.end_of_num(i)
            if countUp == True:
                print(f'the {i + 1}{end} value in the sequence is: ' + str(startValue))

        if not countUp == True:
            print(f'the {n}{end} value in the sequence is: ' + str(startValue))

    def altfib():
        countUp = False
        startValue = 1
        holdValue = 0
        pastValue = 0
        counter = 0

        value = input('what is the value of the largest number in the fibinachi sequence would you like to know? ')
        ifCountUp = input(f'would you like know all values up to {value}: ')
        if ifCountUp in ['y','Y','Yes','yes']:
            countUp = True
        else:
            countUp = False
        n = value

        while(startValue < int(n)):
            startValue = startValue + holdValue
            holdValue = holdValue + pastValue
            pastValue = startValue - holdValue
            counter += 1
            end = Utility.end_of_num(counter)
            if countUp == True:
                print(f'the {counter + int(1)}{end} value in your sequence is: ' + str(startValue))

        if not countUp == True:
            if startValue == int(n):
                print(f'{startValue} is the {counter}{end} value in the sequence')
            else:
                print(f'The closest value below {n} in your sequence is: {holdValue}')
                print(f'The closest value above {n} in your sequence is: {startValue}')

