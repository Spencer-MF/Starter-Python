import time
from datetime import date

class Database:

    def __init__(self):
        self.names_list = []
        self.names = {}
        self.phone_numbers = {}
        self.ages = {}
        self.notes = {}
        self.data_directory = {'Name':self.names, 'Phonenumber':self.phone_numbers, 'Age':self.ages, 'Notes': self.notes}


    def input_data(self):
        print('please add the fallowing information about if you '"don't know press enter or type None")
        for data_type in self.data_directory.keys():
            print(f'Enter the {data_type}:')
            if data_type == 'Name':
                in_name = input() 
                self.names_list.append(in_name)
                data = self.data_directory[data_type]
                data[in_name] = in_name
            else:
                in_data = input()
                data = self.data_directory[data_type]
                name = self.names_list[-1]
                data[name] = in_data

    def find_info_person(self):
        print('What person would you like to finds info')
        name = input()
        for data_type, data in self.data_directory.items():
            print(f'{data_type}: {data[name]}')

    def remove_indivual(self):
        print('What person would you like to remove?')
        name = input()
        idx = self.names_list.index(name)
        person = self.names_list.pop(idx)
        for data in self.data_directory.values():
            del data[person]
        print('done!')

    def print_full_table(self):
        data_list = []
        for data_type, data_pointer in self.data_directory.items():
            for data in data_pointer.values():
                data_list.append(data)
            print(f'{data_type}: {data_list}')
            data_list.clear()

class FrontEnd:

    def __init__(self, db, im):
        self.db = db
        self.im = im

    def control_panal(self):
        print('This is the control panal for this database')
        print('If you would like to add people press 1 if you would like to remove people press 2')
        print("if you would like to see the full database press 3 if you would like to find a spasific person info press 4")
        print('if you would like to import a file (this file has to be structed for this database) press 0')
        while True:
            admin_choice = input()
            if admin_choice == '1':
                self.add_people()
            elif admin_choice == '2':
                self.remove_people()
            elif admin_choice == '3':
                db.print_full_table()
            elif admin_choice == '4':
                db.find_info_person()
            elif admin_choice == '0':
                im.what_file()
            else:
                print('Invaid input')
            cont = input('If you would like to continue press enter: ')
            if cont != '':
                break


    def add_people(self):
        while True:
            db.input_data()
            cont = input('To add another person press Enter: ')
            if cont != '':
                break

    def remove_people(self):
        while True:
            db.remove_indivual()
            cont = input('To remove another person press Enter: ')
            if cont != '':
                break

class Export:

    def __init__(self, db):
        self.db = db
        self.current_time = None
        self.current_date = None

    def export_control(self):
        print('Would you like to export data\n Yes or No')
        while True:
            export = input()
            if export in ['yes', 'y', 'Y', 'Yes']:
                self.export_data_choice()
            else:
                print('All data not exported will be deleted when this program closes')
                cont = input('press enter to accept')
                if cont == '':
                    break

    def export_data_choice(self):
        print('Would you like to export to a new or existing file?')
        file_choice = input()
        if file_choice in ['New', 'new', 'n', 'N']:
            self.export_data_new()
        else:
            self.export_data_existing()
        
    def export_data_new(self):
        file_name = input('what would you like to name the file?\n')
        open(f'{file_name}.txt', 'w')
        self.write_full_table(file_name)

    def export_data_existing(self):
        file_name = input('What is the name of the file you want to save to?\n')
        self.write_full_table(file_name)

    def write_full_table(self, file_name):
        self.get_time_and_date()
        with open(f'{file_name}.txt', 'a') as f:
            f.write(f'\n\n{self.current_date} {self.current_time}\n\n')
            for people in db.names_list:
                for data_type in db.data_directory.keys():
                    f.write(f'{data_type}: ')
                    data_folder = db.data_directory[data_type]
                    data = data_folder[people]
                    f.write(str(data))
                    f.write('\n')
                f.write('\n')
    
    def get_time_and_date(self):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        self.current_time = current_time
        today = date.today()
        self.current_date = today

class ImportFile:
    def __init__(self, db):
        self.db = db

    def what_file(self):
        file_name = input('What is the name of the file that you would like to read?\n')
        self.read_file(file_name)

    def read_file(self, file_name):
        with open(f'{file_name}.txt', 'r') as f:
            lines = f.readlines()
            self.populate_database(lines)

    def populate_database(self, lines):
        current_name = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('Name:'):
                current_name = line.split(':')[1].strip()
                if current_name not in db.names_list:
                    db.names_list.append(current_name)
                db.names[current_name] = current_name
            elif line.startswith('Phonenumber:'):
                if current_name:
                    db.phone_numbers[current_name] = line.split(':')[1].strip()
            elif line.startswith('Age:'):
                if current_name:
                    db.ages[current_name] = line.split(':')[1].strip()
            elif line.startswith('Notes:'):
                if current_name:
                    db.notes[current_name] = line.split(':')[1].strip()

db = Database()
im = ImportFile(db)
fr = FrontEnd(db, im)
ex = Export(db)
def main():
    fr.control_panal()
    ex.export_control()

if __name__ == '__main__':
    main()
