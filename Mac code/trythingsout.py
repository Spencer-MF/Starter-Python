from datetime import date
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from hashlib import sha256

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


def text_to_hex(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    binary = ' '.join(format(ord(char), '08b') for char in text)
    with open('binary_version.txt', 'w') as f:
        f.write(binary)

def read_binary_from_file(input_path):
    with open(input_path, 'r') as file:
        binary_data = file.read()
    return binary_data

def binary_to_text(binary_data):
    binary_values = binary_data.split(' ')
    text = ''.join(chr(int(bv, 2)) for bv in binary_values)
    with open('plain_text.txt', 'w') as f:
        f.write(text)

def txt_to_bin(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    print(text)
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text)
    print(ciphertext)

# Encryption function
def encrypt_text(plain_text, key):

    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the plain text to be a multiple of 16 bytes
    padded_text = pad(plain_text.encode(), AES.block_size)

    # Encrypt the padded text
    encrypted_text = cipher.encrypt(padded_text)

    # Return the IV and the encrypted text
    return iv + encrypted_text

# Decryption function
def decrypt_text(encrypted_text, key):
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

def encrpytion_test():
    # Example usage
    plain_text = "This is a secret message."
    key = sha256('chyper'.encode('utf-8')).digest()
    """
    # Encrypt the text
    encrypted_text = encrypt_text(plain_text, key)
    print(f"Encrypted text (bytes): {encrypted_text}")
    """
    file_name = 'test'
    with open(f'{file_name}.mf', 'rb') as f:
        encrypted_text = f.read()
    print(encrypted_text)
    print(key)

    # Decrypt the text
    try:
        decrypted_text = decrypt_text(encrypted_text, key)
        print(f"Decrypted text: {decrypted_text}")
    except ValueError:
        print('no')

def binary_counter():
    bi_list = []
    x = 1
    for i in range(5):
        bi_list.append(0)
    print(bi_list)

def generate_binary_list(n):
  return [bin(i)[2:] for i in range(n + 1)]


print(generate_binary_list(32))
