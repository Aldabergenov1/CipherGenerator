import dicts_and_lists

def Ceaser(string, step):
    cipher = ''
    for char in string:
        if char != ' ' and char not in dicts_and_lists.symbols:
            if char in dicts_and_lists.letters_lower:
                if ord(char) + step > 122:
                    ascii_index = ord(char) + step - 26
                    cipher += chr(ascii_index)
                else:
                    cipher += chr(ord(char) + step)
            elif char in dicts_and_lists.letter_upper:
                if ord(char) + step > 90:
                    ascii_index = ord(char) + step - 26
                    cipher += chr(ascii_index)
                else:
                    cipher += chr(ord(char) + step)
        else:
            cipher += char
    return cipher

def Morse(string):
    cipher = ''
    upper_string = string.upper()
    for char in upper_string:
        if char != ' ':
            cipher += dicts_and_lists.morse_dict[char]
        else:
            cipher += ' '
    return cipher

def Binary(string):
    cipher = ''
    for char in string:
        if char != ' ':
            cipher += bin(ord(char)) + ' '
        else: 
            cipher += ' '
    cipher = cipher.replace('b', '')
    return cipher

def Atbash(string):
    cipher = ''
    for char in string:
        if char != ' ':
            cipher += dicts_and_lists.atbash_dict[char]
        elif char not in dicts_and_lists.atbash_dict: 
            cipher += char
    return cipher

print('Hello! Which of the popular ciphers do you want to choose?')

while True:
    print('1 - Caesar Cipher', '2 - Morse Code', '3 - Binary Code', '4 - Atbash Cipher', sep = '\n')
    choise = int(input())
    while choise not in [1, 2, 3, 4]:
        print('Error! Enter the correct value!')
        choise = int(input())
    string = str(input('Enter the sentence you want to encrypt(in English): '))
    if choise == 1:
        step = int(input('Enter the step for the cipher(from 1 to 26): '))
        print(Ceaser(string, step))
    elif choise == 2:
        print(Morse(string))
    elif choise == 3:
        print(Binary(string))
    elif choise == 4:
        print(Atbash(string))
    print('Would you like to continue?', '1 - Yes', '2 - No')
    choise2 = int(input())
    if choise2 == 1:
        pass
    elif choise2 == 2:
        print('Glad to help! Goodbye!')
        break
    else:
        print('Error! Enter the correct value!')