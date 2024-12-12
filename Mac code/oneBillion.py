from Nicetohaves import Utility

class zipBomb:

    def __init__(self, ut):
        self.ut = ut
        self.file_name = 'test'
        self.toggle = True

    def write_file(self):
        self.create_file()
        print('done')

    def create_file(self):
        with open(f'{self.file_name}.txt', 'w') as f:
            if self.toggle:
                self.right_10_power_10_power_10(f)
            else:
                self.right_one_billion_lines(f)
            f.close

    def right_one_billion_lines(self, f):
        for i in range(1000000):
            end = ut.end_of_num(i-1)
            f.write(f'{i}{end} line\n')

    def right_10_power_10_power_10(self, f):
        f.write('1')
        for i in range(100000):
            for j in range(100000):
                end = ut.end_of_num(i+j-1)
                f.write('0')
            f.write('\n')

ut = Utility
ob = zipBomb(ut)

def main():
    ob.write_file()

if __name__ == '__main__':
    main()