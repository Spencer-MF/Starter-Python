# This version of the code only works on macOS, as signal handling differs between macOS and Windows.

import time
import sys
import signal
import os
import fileinput
from datetime import date
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

TIMEOUT = 5

class Database:

    def __init__(self):
        self.names_list = []
        self.names = {}
        self.phone_numbers = {}
        self.dob = {}
        self.notes = {}
        self.data_directory = {'Name':self.names, 'Phonenumber':self.phone_numbers, 'Date of Birth':self.dob, 'Notes': self.notes}

        self.password_manager = {}

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
                    print('mm-dd-yyyy format (with dashes)')
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
        print('What type of info would you like to change?\n Name, Phonenumber, Date of Birth, or Notes\n')
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
            if self.lists_overlap(data_type, ['3', 'date of birth', 'date', 'Date of Birth', 'birth', 'Date', 'birth', 'Date of birth', 'dob', 'DoB']):
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
        new_age = input(f"What would you like to change {name}'s date of birth to?\nmm-dd-yyyy format (with dashes)\n")
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
        delta_year = int(today_list[0]) - int(dob[2])
        delta_month = int(today_list[1]) - int(dob [0])
        delta_day = int(today_list[2]) - int(dob[1])
        if delta_month < 0 and delta_day < 0:
            delta_year -= 1
        return delta_year, delta_month, delta_day
        
    def time_till_birthday(self, name):
        dy, dm, dd = self.age_calc(name)
        dm *= -1
        dd *= -1
        if dm < 0:
            dm += 12
        if dm == 0 and dd < 0:
            dm += 11
            dd += self.month()
        elif dd < 0:
            dm -= 1
            dd -= self.month()
        return dm, dd, dy + 1

    def closest_birthday(self):
        min_time = []
        min_time_name = []
        x_way_tie = 0
        min_time_name_tie = []
        ages = []
        for name in self.names_list:
            dm, dd, dy = self.time_till_birthday(name)
            days_converted_from_months = self.month_to_day(dm)
            days = dd + days_converted_from_months
            if not min_time:
                min_time.append(days)
                min_time_name.append(name)
            elif days < min(min_time)-1:
                min_time.append(days)
                min_time_name.append(name)
            elif days == min(min_time):
                    x_way_tie += 1
                    min_time.append(days)
                    min_time_name.append(name)
        for i in range(x_way_tie + 1):    
            name = min_time_name[-(i + 1)]
            min_time_name_tie.append(name)
            mm, dd, turing_years_old = self.time_till_birthday(name)
            ages.append(turing_years_old)
        name = min_time_name[-1]
        mm, dd, dy = self.time_till_birthday(name)
        if not ages:
            ages.append(dy)
        return min_time_name_tie, mm, dd, ages

    def in_age_range(self):
        minmax = str(input('Type the min age then a space then the max age for no min or max type None or type - instead:\n'))
        min_and_max = minmax.split()
        minimum = min_and_max[0]
        maximum = min_and_max[1]
        if minimum == None or minimum == '-':
            minimum = 0
        if maximum == None or maximum == '-':
            maximum = 1000000
        names = []
        for name in self.names_list:
            years_old, ignor1, ignor2 = self.age_calc(name)
            if int(minimum) -1  < int(years_old) < int(maximum) + 1:
                names.append(name)
        if not names:
            names.append('No one in age range')
        return names, minimum, maximum

    def password_control(self, file_name, new_password):
        old_password = self.password_manager[file_name]
        while True:
            new_password = sha256(new_password.encode('utf-8')).hexdigest()
            if old_password != new_password:
                self.find_and_replace(file_name, f'{file_name}: {old_password}', f'{file_name}: {new_password}')
                break
            else:
                new_password = input('New password can not be the same as the old password')

    def find_and_replace(self, file_name, find, replace):
        with fileinput.input(f'{file_name}.txt', inplace=True) as file:
            for line in file:
                new_line = line.replace(find, replace)
                print(new_line, end='')

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

    def __init__(self, db, im, ed):
        self.db = db
        self.im = im
        self.ed = ed

    def control_panal(self):
        print('This is the control panal for this database')
        print('If you would like to add people press 1 if you would like to remove people press 2')
        print("if you would like to see the full database press 3 if you would like to find a spasific person info press 4")
        print('if you would like to know the amount of entries press 5 if you would like to edit a person press 6')
        print('if you would like to know about the ages of the people press 7 if you would like to change the password on a file press 8')
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
            elif admin_choice == '8':
                self.change_password()
            elif admin_choice == '0':
                im.what_file('read')
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
                cont = input("To find another person's agepress Enter: ")
            else:
                print(f'{name} not found in database')
            if cont != '':
                break

    def next_birthday_specific(self):
        name = input("Who's next birthday would you like to know?\n")
        mm, dd, dy = db.time_till_birthday(name)
        print(f"There are {mm} months and {dd} days till {name}'s next birthday!\n{name} is turning {dy} years old")

    def people_age_range(self):
        responce = 0
        name, minimum, maximum = db.in_age_range()
        total_poeple = len(name)
        is_or_are = 'are'
        if total_poeple > 1:
            names_list = ', '.join(name[:-1]) + ', and ' + name[-1]
        else:
            names_list = name[0]
            is_or_are = 'is'
        if int(minimum) < 1:
            responce += 1
        if int(maximum) > 10000:
            responce += 2
        if responce == 0:
            print(f'{total_poeple} {is_or_are} in the age range {minimum} to {maximum} years old\n{names_list}')
        elif responce == 1:
            print(f'{total_poeple} {is_or_are} younger than {maximum} years old\n{names_list}')
        elif responce == 2:
            print(f'{total_poeple} {is_or_are} older than {minimum} years old\n{names_list}')
        else:
            print(f'{total_poeple} {is_or_are} in the database with an age\n{names_list}')

    def next_birthday(self):
        name, mm, dd, dy = db.closest_birthday()
        name = self.merge_lists(name, dy)
        num_people = len(name)
        has_or_have = 'have'
        person_or_people = 'people'
        if num_people > 1:
            names_list = ', '.join(name[:-1]) + ', and ' + name[-1]
        else:
            names_list = name[0]
            has_or_have = 'has'
            person_or_people = 'person'
        print(f'{num_people} {person_or_people} {has_or_have} the closest birthday!\nIt is in {mm} months and {dd} days\nThey are {names_list}')
    
    def change_password(self):
        im.what_file('change the password to')
        new_password = input('what would you like the new password to be?\n')
        db.password_control(im.file, new_password)
        ed.encrypt_master(im.file)
        os.remove(f'{im.file}.txt')

    def merge_lists(self, list1, list2):
    # Ensure both lists are of the same length
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length")
    
    # Merge the lists
        merged_list = [f'{list1[i]} turing {list2[i]} years old' for i in range(len(list1))]
        return merged_list

class Export:

    def __init__(self, db, ed):
        self.db = db
        self.ed = ed
        self.current_time = None
        self.current_date = None
        self.password = None
        self.password_switch = False

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
        elif file_choice in ['existing', 'Existing', 'old', 'Old']:
            self.export_data_existing()
        
    def export_data_new(self):
        file_name = input('what would you like to name the file?\n')
        password_control = input('Would you like to password protect your file\nYes or No\n')
        if password_control in ['y', 'Y', 'yes', 'Yes']:
            self.password = input('Enter your passowrd:\n')
            self.password_switch = True
            self.password = sha256(self.password.encode('utf-8')).hexdigest()
            db.password_manager[file_name] = self.password
        open(f'{file_name}.txt', 'w')
        self.write_full_table(file_name)
        ed.encrypt_master(file_name)

    def export_data_existing(self):
        file_name = input('What is the name of the file you want to save to?\n')
        ed.decrypt_file_master(file_name)
        if ed.confirm_file:
            if ed.password_fail:
                self.export_control()
            self.write_full_table(file_name)
            ed.encrypt_master(file_name)

    def write_full_table(self, file_name):
        self.get_time_and_date()
        with open(f'{file_name}.txt', 'a') as f:
            f.write(ed.file_format_encode)
            if self.password_switch:
                f.write(f'\n\n{self.current_date} {self.current_time}\n')
                f.write(f'{file_name}: {self.password}\n\n')
            else:
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

    def file_check(self, file_name):
        with open(f'{file_name}.txt', 'r') as f:
            lines = f.readlines()
            file_format = lines[0]
            if not file_format.startswith(ex.file_format_encode):
                print('Incompatable file format')
                print('Returing to main menu')
                self.compatiable_file = False  

class ImportFile:
    def __init__(self, db, ed):
        self.db = db
        self.ed = ed
        self.file = None
        self.question_type = False

    def what_file(self, question_txt):
        file_name = input(f'What is the name of the file that you would like to {question_txt}?\n')
        if question_txt != 'read':
            self.question_type = True
        self.file = file_name
        ed.decrypt_file_master(file_name)
        if ed.confirm_file:
            with open(f'{file_name}.txt', 'r') as f:
                lines = f.readlines()
                self.populate_database(lines, file_name)            

    def populate_database(self, lines, file_name):
        current_name = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith(file_name):
                pw_hash = line.split(':')[1].strip()
                db.password_manager[file_name] = pw_hash
            elif line.startswith('Name:'):
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
        if not self.question_type:
            os.remove(f'{file_name}.txt')
            self.question_type = False

class TimeoutException(Exception):
    pass

class EncryptDecrypt:
    
    def __init__(self, db, te):
        self.db = db
        self.te = te

        self.file_format_encode = self.proprietary_file_format()
        self.import_fail = False
        self.password_fail = False
        self.compatiable_file = True
        self.decryption_tries = 0
        self.confirm_file = False

    def encrypt_master(self, file_name):
        password = input('Enter the Encrpytion Key\n(for encrpytion)\n')
        encrypted_txt = self.encryption(file_name, password)
        os.remove(f'{file_name}.txt')
        self.write_encrpyed_file(file_name, encrypted_txt)        
    
    def encryption(self, file_name, key):
        key = sha256(key.encode('utf-8')).digest()
        with open(f'{file_name}.txt', 'r') as f:
            text = f.read()
            if not text.startswith(self.file_format_encode):
                print('Incorrect Encrpytion Key try again')
                self.encrypt_master(file_name)
        # Generate a random initialization vector (IV)
        iv = get_random_bytes(16)
        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # Pad the plain text to be a multiple of 16 bytes
        padded_text = pad(text.encode(), AES.block_size)
        # Encrypt the padded text
        encrypted_text = cipher.encrypt(padded_text)
        # Return the IV and the encrypted text
        return iv + encrypted_text
    
    def write_encrpyed_file(self, file_name, text):
        with open(f'{file_name}.mf', 'wb') as f:
            f.write(text)
    
    def proprietary_file_format(self):
        pff= "This is Spencer's file format"
        pff = sha256(pff.encode('utf-8')).hexdigest()
        return ' '.join(['Proprietary file:', pff])

    def decrypt_file_master(self, file_name):
        text = self.decrypt_file(file_name)
        self.temp_txt_file(file_name, text)
        self.read_file(file_name)
    
    def decrypt_file(self, file_name):
        decryption_tries = 0
        key = input('Enter the Encrpytion Key:\n(for decrpytion)\n')
        with open(f'{file_name}.mf', 'rb') as f:
            encrypted_text = f.read()
        while True:
            try:
                key = sha256(key.encode('utf-8')).digest()
                decrypted_text = self.decrypt_text(encrypted_text, key)
                return decrypted_text
            except ValueError:
                print('incorrect Encryption Key try again')
                decryption_tries += 1
                print(f'{3 - decryption_tries} attempts left')
                if decryption_tries == 3:
                    print('Too many failed atempts')
                    print('program ending')
                    sys.exit()    
                key = input('Enter the Encrpytion Key:\n(for decrpytion)\n')

    def temp_txt_file(self, file_name, text):
        with open(f'{file_name}.txt', 'w') as f:
            f.write(text)

    def decrypt_text(self, encrypted_text, key):
        # Extract the initialization vector (IV) from the encrypted text
        iv = encrypted_text[:16]
        encrypted_text = encrypted_text[16:]
        # Create AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # Decrypt the encrypted text
        padded_text = cipher.decrypt(encrypted_text)
        # Unpad the decrypted text
        plain_text = unpad(padded_text, AES.block_size)
        return plain_text.decode()

    def read_file(self, file_name):
        with open(f'{file_name}.txt', 'r') as f:
            lines = f.readlines()
            self.file_check(lines)
            if self.compatiable_file:
                self.password_read(lines, file_name)
                if not self.import_fail:
                    self.populate_trigger()

    def populate_trigger(self):
        ed.confirm_file = True 

    def file_check(self, lines):
        file_format = lines[0]
        if not file_format.startswith(self.file_format_encode):
            print('Incompatable file format')
            print('Returing to main menu')
            self.compatiable_file = False 

    def password_read(self, lines, file_name):
        signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(TIMEOUT)
        password_fail = 0
        pw = lines[3]
        if pw.startswith(file_name):
            print('This file is password protected')
            print(f'please enter the password for {file_name}')
            while True:
                signal.alarm(TIMEOUT)
                unlock_password = self.input_password(file_name)
                if unlock_password != None:
                    unlock_password = sha256(unlock_password.encode('utf-8')).hexdigest()
                    true_password = pw.split(':')[1].strip()
                    if true_password == unlock_password:
                        signal.alarm(0)
                        break
                    password_fail += 1
                else:
                    self.import_fail = True
                    self.password_fail = True
                    break
                print(f'try again {3 - password_fail}')
                if password_fail == 3:
                    print('Too many failed atempts')
                    print('program ending')
                    self.import_fail = True
                    break    

    def input_password(self, file_name):
        try:
            password = input()
            return password
        except TimeoutException:
            os.remove(f'{file_name}.txt')
            print('You took to long to input password')
            return None          

    def timeout_handler(self, signum, frame):
        raise TimeoutException

db = Database()
te = TimeoutException()
ed = EncryptDecrypt(db, te)
ex = Export(db, ed)
im = ImportFile(db, ed)
fr = FrontEnd(db, im, ed)
def main():
    fr.control_panal()
    ex.export_control()

if __name__ == '__main__':
    main()
    