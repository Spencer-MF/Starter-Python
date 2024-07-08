from datetime import date

def add_list():
    n = input('Enter all the number you want to add seperated by a space: ')
    lst = n.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    s = sum(lst)
    print(s)

in_lst = [1,2,3,4]

def list_2x(in_lst):
    for i in range (len(in_lst)):
        in_lst[i] *= 2
    print(in_lst)

def del_test(lst):
    del lst[0], lst[-1]

def replace_list_test(lst):
    lst[0] = 5

def age_calc_test(dob):
    today = str(date.today())
    today_list = today.split('-')
    dob = dob.split('-')
    delta_year = int(today_list[0]) - int(dob[0])
    delta_month = int(today_list[1]) - int(dob [1])
    delta_day = int(today_list[2]) - int(dob[2])
    if delta_month < 0 and delta_day < 0:
        delta_year -= 1
    print(delta_year, delta_month, delta_day)
    print(f'you are {delta_year} years old')

def leap_year(yyyy, bool):
        today = str(date.today())
        today_list = today.split('-')
        if bool:
            yyyy = int(today_list[0])
        yy00 = yyyy % 100
        if yy00 != 0:
            if yyyy % 4 == 0:
                print('true')
                return True
        elif yyyy % 400 == 0:
            print('true')
            return True
        print('false')
    
def month_to_day(dm):
        dm *= -1
        if dm < 0:
            dm += 12
        days = 0
        today = str(date.today())
        today_list = today.split('-')
        mm = int(today_list[1])
        for i in range(int(dm)):
            mm += i
            if mm in [1, 3, 5, 7, 8, 12]:
                days += 31
            elif mm in [2]:
                if leap_year(2024, True):
                    days += 29
                days += 28
            else:
                days += 30
        print(days)

def time_till_birthday(dm, dd):
        dm *= -1
        if dm < 0:
            dm += 12
        if dd > 0:
            dm -= 1
            dd += 30
        else:
            dd *= -1
        print(dm, dd)
