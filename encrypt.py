# Reads a plaintext string from a text file.
 # read from file - https://www.w3schools.com/python/python_file_open.asp
# Encrypts the string using a Caesar cipher with a randomly generated key. You can make your program only change the letters A-Z and leave other characters (numbers, punctuation, spaces) unchanged.
 # random integer - https://docs.python.org/3/library/random.html
# Saves the ciphertext to a new text file.

import random

def main():
    with open("example.txt","r") as file:
        plaintext = file.read()

    encryption = encrypt(plaintext.lower(), generate_key())

    with open("coded_message.txt","w") as new_file:
        new_file.write(encryption)


def generate_key():
    return random.randint(1, 43)

def encrypt(plaintext, key):
    characters = "abcdefghijklmnopqrstuvwxyz,.!?'()0123456789 "
    encoded = ""
    for i in range(len(plaintext)):
        alphabet_index = characters.index(plaintext[i])
        new_letter_index = (alphabet_index + key) % 44
        encoded += characters[new_letter_index]
    return encoded


main()