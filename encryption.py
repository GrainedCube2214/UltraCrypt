import sys

Morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', '': '', '!': '!',
              '@': '@', '#': '#', '$': '$', '%': '%', '^': '^',
              '&': '&', '*': '*', '+': '+','=': '=', ',': ',',
              '<': '<', '>': '>', ';': ';', ':': ':', '"': '"',
              "'": "'", '[': '[', ']': ']', '{': '{', '}': '}'}

vig_dict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12,
            'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24,
            'z': 26, '.': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, '6': 33, '7': 34, '8': 35, '9': 36,
            '!': '!', '@': '@', '#': '#', '$': '$', '%': '%',
            '^': '^', '&': '&', '*': '*', '(': '(', ')': ')',
            '+': '+', '0': '0', '=': '=', ',': ',', '/': '/', '<': '<',
            '>': '>', '?': '?', ';': ';', ':': ':', '"': '"',
            "'": "'", '[': '[', ']': ']', '{': '{', '}': '}'}

inv_morse = {v: k for k, v in Morse_code.items()}

hsc_dict = {'a': 'q', 'c': 'w', 'b': 'e', 'e': 'r', 'd': 't', 'g': 'y', 'f': 'u', 'i': 'i', 'h': 'o', 'k': '5',
            'j': 'p', 'm': '2', 'l': 'a', 'o': 's', 'n': 'd', 'q': 'f', 'p': 'g', 's': 'h', 'r': '0', 'u': 'j',
            't': 'k', 'w': 'l',
            'v': '1', 'y': '8', 'x': '3', 'z': 'z', '.': 'x', '1': '6', '2': 'c', '3': 'v', '4': '7', '5': 'b',
            '6': 'n', '7': '4', '8': 'm', '9': '9', ' ': ' ',
            '!': '!', '@': '@', '#': '#', '$': '$', '%': '%',
            '^': '^', '&': '&', '*': '*', '(': '(', ')': ')',
            '+': '+', '=': '=', ',': ',', '/': '/', '<': '<',
            '>': '>', '?': '?', ';': ';', ':': ':', '"': '"',
            "'": "'", '[': '[', ']': ']', '{': '{', '}': '}'}

inv_hsc_dict = {v: k for k, v in hsc_dict.items()}

at_bash_dict = {'a': 'z', 'b': 'y', 'c': 'x', ' ': ' ', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r',
                'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', '0': '9', '1': '8', '2': '7', '3': '6', '4': '5',
                '!': '!', '@': '@', '#': '#', '$': '$', '%': '%',
                '^': '^', '&': '&', '*': '*', '(': '(', ')': ')',
                '+': '+', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                '=': '=', ',': ',', '/': '/', '<': '<',
                '>': '>', '?': '?', ';': ';', ':': ':', '"': '"',
                "'": "'", '[': '[', ']': ']', '{': '{', '}': '}'}

at_bash_dict_inv = {v: k for k, v in at_bash_dict.items()}

at_bash_dict.update(at_bash_dict_inv)


def mlk(x):
    g = ''
    for i in x:
        g += i
    return g


def morse_enc(string2):
    cipher = ''
    for i in string2:
        if i !=' ':
            cipher = cipher + Morse_code[i.upper()]
            cipher = cipher + ' '
        else:
            cipher = cipher + i
    return cipher


def morse_dec(string1):
    cipher = ''
    string1 = string1 + ' '
    list1 = []
    for i in string1:
        if i != ' ':
            list1 += [i]
        else:
            s = mlk(list1)
            cipher = cipher + inv_morse[s]
            cipher = cipher + ' '
            list1 = []
    v = ''
    c = 0
    cipher = cipher + ' '
    while c < len(cipher):
        if c == len(cipher) - 1:
            break
        elif cipher[c] != ' ':
            v = v + cipher[c]
        elif cipher[c] == ' ':
            if cipher[c + 1] == ' ':
                v = v + ' '
        c = c + 1
    return v.lower()


'''
def diff_hellman_dec(string):
    flag = True
    while flag == True:
        s=0
        p = int(input("enter value of prime number p: "))
        for i in range(1, p):
            if p%i==0:
                s+=1
        if s == 1:
            flag = False
        else:
            print("enter only prime number")

    q = int(input("enter value of generator q"))
    a = int(input("enter whole number a lesser than p: "))
    b = int(input("enter whole number b lesser than p: "))
    a_star = (q**a) % p
    b_star = (q**b) % p
    x1 = ((b_star)**a) % p
    x2 = ((a_star)**b) % p
    print(x1, x2) '''

a = ''


def custom_enc(string3, gen):
    b = ''
    for i in string3:
        b = b + chr(ord(i) + gen)
    b = b[::-1]
    return b


def custom_dec(string4, gen):
    b = ''
    for i in string4:
        b = b + chr(ord(i) - gen)
    b = b[::-1]
    return b


def cc2_enc(string5, key1):
    enc = ''
    f = 0
    for i in string5:
        if f == len(key1):
            f = 0
        enc = enc + (chr((ord(i) + vig_dict[key1[f].lower()])))
        f = f + 1
    return enc


def cc2_dec(string6, key2):
    enc = ''
    f = 0
    for i in string6:
        if f == len(key2):
            f = 0
        enc = enc + (chr((ord(i) - vig_dict[(key2[f]).lower()])))
        f = f + 1
    return enc


def hsc_enc(string7):
    enc = ''
    for i in string7:
        enc = enc + hsc_dict[i]
    return enc


def hsc_dec(string8):
    dec = ''
    for i in string8:
        dec = dec + inv_hsc_dict[i]
    return dec


def word_to_list(string9):
    lo = []
    f = 0
    v = 0
    for i in string9:
        if f == 0:
            lo.append('')

        if f < 2:
            lo[v] = lo[v] + i
        else:
            v = v + 1
            f = 0
    return lo


def four_square_enc(j):
    l1 = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'k'], ['l', 'm', 'n', 'o', 'p'], ['q', 'r', 's', 't', 'u'],
          ['v', 'w', 'x', 'y', 'z']]
    l2 = [['p', 'l', 't', 'x', 'u'], ['a', 'i', 'r', 'z', 'y'], ['b', 'e', 'g', 'v', 'h'], ['c', 'k', 'd', 'm', 'w'],
          ['q', 'f', 'o', 's', 'n']]
    l3 = [['c', 'h', 'k', 'o', 's'], ['d', 'g', 'u', 'p', 'n'], ['a', 'e', 'q', 'i', 'f'], ['b', 'm', 'y', 'w', 'x'],
          ['z', 'u', 't', 'v', 'r']]
    l4 = l1
    dec = ''
    spl_chr = 'j !@#$%^&*()+1234567890=,/<>?;:"\'[]{}'
    for i in j:
        if len(i) == 2 and i[0] not in spl_chr and i[1] not in spl_chr:
            l1in = []
            l4in = []
            for x in range(0, 5):
                for y in range(0, 5):
                    if l1[x][y] == i[0]:
                        l1in = l1in + [x]
                        l1in = l1in + [y]
            for x in range(0, 5):
                for y in range(0, 5):
                    if l4[x][y] == i[1]:
                        l4in = l4in + [x]
                        l4in = l4in + [y]
            dec = dec + l2[l1in[0]][l4in[1]]
            dec = dec + l3[l4in[0]][l1in[1]]
        else:
            dec = dec + i
    return  dec


def four_square_dec(j):
    l1 = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'k'], ['l', 'm', 'n', 'o', 'p'], ['q', 'r', 's', 't', 'u'],
          ['v', 'w', 'x', 'y', 'z']]
    l2 = [['p', 'l', 't', 'x', 'u'], ['a', 'i', 'r', 'z', 'y'], ['b', 'e', 'g', 'v', 'h'], ['c', 'k', 'd', 'm', 'w'],
          ['q', 'f', 'o', 's', 'n']]
    l3 = [['c', 'h', 'k', 'o', 's'], ['d', 'g', 'u', 'p', 'n'], ['a', 'e', 'q', 'i', 'f'], ['b', 'm', 'y', 'w', 'x'],
          ['z', 'u', 't', 'v', 'r']]
    l4 = l1
    dec = ''
    spl_chr = 'j !@#$%^&*()+1234567890=,/<>?;:"\'[]{}'
    for i in j:
        if len(i) == 2 and i[0] not in spl_chr and i[1] not in spl_chr:
            l2in = []
            l3in = []
            for x in range(0, 5):
                for y in range(0, 5):
                    if l2[x][y] == i[0]:
                        l2in = l2in + [x]
                        l2in = l2in + [y]
            for x in range(0, 5):
                for y in range(0, 5):
                    if l3[x][y] == i[1]:
                        l3in = l3in + [x]
                        l3in = l3in + [y]
            dec = dec + l1[l2in[0]][l3in[1]]
            dec = dec + l4[l3in[0]][l2in[1]]
        else:
            dec = dec + i
    return dec


def sch(string10):
    k = string10.split()
    j = []
    for i in k:
        m = 0
        b = 2
        while b < (len(i) + 2):
            s = ''
            s = s + i[int(m): int(b)]
            j = j + [s]
            m = m + 2
            b = b + 2
        j = j + [' ']
    return j


def at_bash(string11):
    string11 = string11.lower()
    enc = ''
    for i in string11:
        enc = enc + at_bash_dict[i]
    return enc

'''
print()
print("-------------------------------------------------------------------------------------")
print("                             Encryption And Decryption                               ")
print("-------------------------------------------------------------------------------------")
print('\n')
flag = True
ref = 0
jac = 0
while flag is True:
    ref = int(input("Press 1 for encryption, press 2 for decryption, press 0 for exit: "))
    if ref not in [1, 2, 0]:
        print("Enter valid number")
    else:
        flag = False
if ref == 1:
    string = input("Enter string to encrypt: ")
    flag = True
    while flag is True:
        jac = int(input("Press 1 for Morse Code, \nPress 2 for Caesar Cipher, \nPress 3 for advanced Caesar Cipher,"
                        " \nPress 4 for Homo-phonic Substitution Cipher, \nPress 5 for Four Square Cipher,"
                        " \nPress 6  for At_bash Cipher, \nPress 0 for exit, \nEnter Type here: "))
        if jac not in [0, 1, 2, 3, 4, 5, 6]:
            print('Enter valid option')
        else:
            flag = False

    if jac == 1:
        print("String was encrypted to", morse_enc(string))

    elif jac == 2:
        key = int(input("Enter integer key: "))
        print("String was encrypted to", custom_enc(string, key))

    elif jac == 3:
        cc2_enc(string)

    elif jac == 4:
        hsc_enc(string)

    elif jac == 5:
        four_square_enc(sch(string))

    elif jac == 6:
        print("Encrypted string is", at_bash(string))
    elif jac == 0:
        sys.exit()

elif ref == 2:
    string = input("Enter string to decrypt: ")
    flag = True
    while flag is True:
        jac = int(input(
            "Press 1 for Morse Code, \nPress 2 for Caesar Cipher, \nPress 3 for advanced Caesar Cipher,"
            " \nPress 4 for Homo-phonic Substitution Cipher, \nPress 5 for Four Square Cipher,"
            " \nPress 6  for At_bash Cipher, \nPress 0 for exit, \nEnter Type here: "))
        if jac not in [0, 1, 2, 3, 4, 5, 6]:
            print('Enter valid option')
        else:
            flag = False

    if jac == 1:
        print("String was decrypted to", end=' ')
        print(morse_dec(string))

    elif jac == 2:
        key = int(input("Enter integer key: "))
        print("String was decrypted to", custom_dec(string, key))

    elif jac == 3:
        cc2_dec(string)

    elif jac == 4:
        hsc_dec(string)

    elif jac == 5:
        four_square_dec(sch(string))

    elif jac == 6:
        print("The string was decrypted to", at_bash(string))
    elif jac == 0:
        sys.exit()

elif ref == 0:
    sys.exit()
'''