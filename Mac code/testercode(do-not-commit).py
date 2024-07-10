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

write_file()
edit_second_line('testerfile')