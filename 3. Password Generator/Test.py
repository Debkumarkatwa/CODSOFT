import random
import string


def pass_generate(min_length, numbers=True, special_char=True):
    min_length = 8 if min_length == '' else int(min_length)
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    password = ''
    criteria = False
    has_number = False
    has_special = False

    while not criteria or len(password) < min_length:
        char = random.choice(characters)
        password += char
        
        if char in digits:
            has_number = True
        elif char in special:
            has_special = True

        criteria = True
        if numbers: criteria = has_number
        if special_char: criteria = (criteria and has_special)

    return password

if __name__ == '__main__':
    length = input('Enter minimum length: ')
    num = bool('1' == input('Want to include Number (press 1)? '))
    schar = bool('1' == input('Want to include Special Character (press 1)? '))
    print( pass_generate(length, num, schar) )