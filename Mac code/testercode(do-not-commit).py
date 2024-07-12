import fileinput

def write_file():
    with open('testerfile.txt', 'w') as f:
        for i in range(10):
            f.write(f'line{i+1}\n')

def edit_second_line(file_name):
    with open(f'{file_name}.txt', 'r') as f:
        lines = f.readlines()
        lines.insert(0,'test\n')
    with open(f'{file_name}.txt', 'w') as f:
        for line in lines:
            f.write(line)
"""
write_file()
edit_second_line('testerfile')
"""
with open('test.txt', 'w') as f:
    f.write('Hello world\n')
    f.write('Hello world\n')
    f.write('test')

def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as file:
        for line in file:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')


replace_in_file('test.txt', 'test', 'confirmed')
