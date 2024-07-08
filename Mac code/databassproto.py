import time
from datetime import date

class Database:

    def __init__(self):
        self.names_list = []
        self.names = {}
        self.phone_numbers = {}
        self.dob = {}
        self.notes = {}
        self.data_directory = {'Name':self.names, 'Phonenumber':self.phone_numbers, 'Date of Birth':self.dob, 'Notes': self.notes}


    def input_data(self):
        print('please add the fallowing information about if you '"don't know press enter or type None")
        for data_type in self.data_directory.keys():
            print(f'Enter the {data_type}:')
            if data_type == 'Name':
                in_name = input() 
                if in_name == '':
                    in_name = None
                self.names_list.append(in_name)
                data = self.data_directory[data_type]
                data[in_name] = in_name
            else:
                if data_type == 'Date of Birth':
                    print('yyyy-mm-dd format (with dashes)')
                in_data = input()
                if in_data == '':
                    in_data = None
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

    def edit_info(self):
        hit = 0
        while True:
            name = input("What person's info would you like to edit?\n")
            if name in self.names_list:
                break
            else:
                print('Invalid name try again')
        print('What type of info would you like to change?\n Name, Phonenumber, Age, or Notes\n')
        invalid = True
        while invalid:
            data_type = self.multi_choice()
            invalid = False
            if self.lists_overlap(data_type, ['1', 'Name', 'name']):
                name = self.name_change(name)
                hit += 1
            if self.lists_overlap(data_type, ['2', 'Phonenumber', 'number', 'phone', 'phonenumber', 'Number', 'Phone']):
                self.number_change(name)
                hit += 1
            if self.lists_overlap(data_type, ['3', 'date of birth', 'date', 'Date of Birth', 'birth', 'Date', 'birth', 'Date of birth']):
                self.dob_change(name)
                hit += 1
            if self.lists_overlap(data_type, ['4', 'Notes', 'notes', 'note', 'Note']):
                self.notes_change(name)
                hit += 1
            if hit == 0:
                print('Invalid input try again')
                invalid = True
            else:
                break
    
    def lists_overlap(self,a, b):
        for i in a:
            if i in b:
              return True
        return False

    def number_change(self, name):
        new_number = input(f"What would you like to change {name}'s phonenumber to?\n")
        self.phone_numbers[name] = new_number

    def dob_change(self, name):
        new_age = input(f"What would you like to change {name}'s date of birth to?\nyyyy-mm-dd format (with dashes)\n")
        self.dob[name] = new_age

    def notes_change(self, name):
        while True:
            choice = input(f'Would you like to add to or replace the notes for {name}')
            if choice in ['1', 'add', 'Add']:
                notes_append = input(f"What would you like to add to {name}'s notes?\n")
                notes_old = self.notes[name]
                self.notes[name] = notes_old + notes_append
                break
            elif choice in ['2', 'replace', 'Replace']:
                notes_replace = input(f"What would you like {name}'s notes to be?\n")
                self.notes[name] = notes_replace
                break
            else:
                print('Invalid input try again')
    
    def multi_choice(self):
        choices = input('Enter all the choices you want seperated by a space:\n')
        choices_lst = choices.split()
        return choices_lst
        
    def name_change(self, name):
        new_name = str(input(f"What would you like to change {name}'s name to?\n"))

        if name not in self.names:
            print(f"Name {name} not found.")
            return None

        for i, people in enumerate(self.names_list):
            if people == name:
                self.names_list[i] = new_name

        self.names[new_name] = new_name
        self.dob[new_name] = self.dob.pop(name)
        self.phone_numbers[new_name] = self.phone_numbers.pop(name)
        self.notes[new_name] = self.notes.pop(name)

        del self.names[name]

        return new_name
                
    def age_calc(self, name):
        dob = str(self.dob[name])
        today = str(date.today())
        today_list = today.split('-')
        dob = dob.split('-')
        delta_year = int(today_list[0]) - int(dob[0])
        delta_month = int(today_list[1]) - int(dob [1])
        delta_day = int(today_list[2]) - int(dob[2])
        if delta_month < 0 and delta_day < 0:
            delta_year -= 1
        return delta_year, delta_month, delta_day
        
    def time_till_birthday(self, name):
        dy, dm, dd = self.age_calc(name)
        dm *= -1
        dd *= -1
        if dm < 0:
            dm += 12
        if dd < 0:
            dm -= 1
            dd -= self.month()
        return dm, dd

    def closest_birthday(self):
        min_time = []
        min_time_name = []
        x_way_tie = 0
        min_time_name_tie = []
        for name in self.names_list:
            dm, dd = self.time_till_birthday(name)
            days_converted_from_months = self.month_to_day(dm)
            days = dd + days_converted_from_months
            if not min_time:
                min_time.append(days)
                min_time_name.append(name)
            elif days < min(min_time)-1:
                if days == min(min_time):
                    x_way_tie += 1
                min_time.append(days)
                min_time_name.append(name)
        for i in range(x_way_tie + 1):    
            name = min_time_name[i]
            min_time_name_tie.append(name)
        name = min_time_name[0]
        mm, dd = self.time_till_birthday(name)
        return min_time_name_tie, mm, dd

    def in_age_range(self):
        minmax = str(input('Type the min age then a space then the max age for no min or max type None or press the spasebar instead:\n'))
        min_and_max = minmax.split()
        minimum = min_and_max[0]
        maximum = min_and_max[1]
        if minimum == None or minimum == ' ':
            minimum = 0
        if maximum == None or maximum == ' ':
            maximum = 1000000
        names = []
        for name in self.names_list:
            years_old, ignor1, ignor2 = self.age_calc(name)
            if int(minimum) -1  < int(years_old) < int(maximum) + 1:
                names.append(name)
        if not names:
            names.append('No one in age range')
        return names, minimum, maximum


    def num_entries(self):
        num = len(self.names_list)
        print(f'There are {num} entries')

    def print_full_table(self):
        data_list = []
        for data_type, data_pointer in self.data_directory.items():
            for data in data_pointer.values():
                data_list.append(data)
            print(f'{data_type}: {data_list}')
            data_list.clear()

    def month(self):
        today = str(date.today())
        today_list = today.split('-')
        mm = today_list[1]
        if mm in ['01', '03', '05', '07', '08', '12']:
            return 31
        elif mm in ['02']:
            if self.leap_year():
                return 29
            return 28
        return 30
    
    def month_to_day(self, dm):
        days = 0
        today = str(date.today())
        today_list = today.split('-')
        mm = int(today_list[1])
        for i in range(int(dm)):
            mm += i
            if mm in [1, 3, 5, 7, 8, 12]:
                days += 31
            elif mm in [2]:
                if self.leap_year():
                    days += 29
                days += 28
            else:
                days += 30
        return days
    
    def years_to_day(self, dy):
        if self.leap_year():
            return 366
        else:
            return 365
    
    def leap_year(self):
        today = str(date.today())
        today_list = today.split('-')
        yyyy = int(today_list[0])
        yy00 = yyyy % 100
        if yy00 != 0:
            if yyyy % 4 == 0:
                return True
        elif yyyy % 400 == 0:
            return True
        return False
        

class FrontEnd:

    def __init__(self, db, im):
        self.db = db
        self.im = im

    def control_panal(self):
        print('This is the control panal for this database')
        print('If you would like to add people press 1 if you would like to remove people press 2')
        print("if you would like to see the full database press 3 if you would like to find a spasific person info press 4")
        print('if you would like to know the amount of entries press 5 if you would like to edit a person press 6')
        print('if you would like to know about the ages of the people press 7')
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
            elif admin_choice == '5':
                db.num_entries()
            elif admin_choice == '6':
                self.edit_people()
            elif admin_choice == '7':
                self.ages_control_panal()
            elif admin_choice == '0':
                im.what_file()
            else:
                print('Invaid input')
            cont = input('If you would like to continue press enter: ')
            if cont != '':
                break

    def ages_control_panal(self):
        print('If you would like to know the ages of people press 1 if you would like to know the time a persons next birthday press 2')
        print('if you would like to know the people in any age range press 3 if you like to know the closest birthday to today press 4')
        while True:
            admin_choice = input()
            if admin_choice == '1':
                self.peoples_age()
            elif admin_choice == '2':
                self.next_birthday_specific()
            elif admin_choice == '3':
                self.people_age_range()
            elif admin_choice == '4':
                self.next_birthday()
            else:
                print('Invaid input')
            cont = input('If you would like to continue in this menue press enter: ')
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

    def edit_people(self):
        while True:
            db.edit_info()
            cont = input('To edit another person press Enter: ')
            if cont != '':
                break
    
    def peoples_age(self):
        while True:
            name = input("Who's age would you like to know?\n")
            if name in db.names_list:
                age, m, d = db.age_calc(name)
                print(f'{name} is {age} years old')
                cont = input('To edit another person press Enter: ')
            else:
                print(f'{name} not found in database')
            if cont != '':
                break

    def next_birthday_specific(self):
        name = input("Who's age would you like to know?\n")
        mm, dd = db.time_till_birthday(name)
        print(f"There are {mm} months and {dd} days till {name}'s next birthday\n")

    def people_age_range(self):
        name, minimum, maximum = db.in_age_range()
        total_poeple = len(name)
        is_or_are = 'are'
        if total_poeple > 1:
            names_list = ', '.join(name[:-1]) + ', and ' + name[-1]
        else:
            names_list = name[0]
            is_or_are = 'is'
        print(f'{total_poeple} {is_or_are} in the age range {minimum} to {maximum} years old\n{names_list}')

    def next_birthday(self):
        name, mm, dd = db.closest_birthday()
        if len(name) > 1:
            names_list = ', '.join(name[:-1]) + ', and ' + name[-1]
        else:
            names_list = name[0]
        print(f'{names_list} has the closest birthday!\nIt is in {mm} months and {dd} days')

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
            elif line.startswith('Date of Birth:'):
                if current_name:
                    db.dob[current_name] = line.split(':')[1].strip()
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
