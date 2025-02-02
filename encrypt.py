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
    return random.randint(1, 25)

def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            alphabet_index = alphabet.index(plaintext[i])
            new_letter_index = (alphabet_index + key) % 26
            encoded += alphabet[new_letter_index]
        else:
            encoded += plaintext[i]
            continue
    return encoded


main()