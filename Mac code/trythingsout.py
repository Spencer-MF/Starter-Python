
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

list_2x(in_lst)