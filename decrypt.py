# Load the encrypted string from the text file.
# Try all 25 possible keys to decrypt the ciphertext, saving each result in a new string.
# Look at all 25 resulting strings. Most of them should be gibberish. Do any of them make sense? Can you figure out which one was the correct key?

import nltk
from nltk.corpus import words
from nltk import word_tokenize

nltk.download('words')

def main():
    with open("coded_message.txt","r") as file:
        coded_message = file.read()

    brute_force_decrypt(coded_message.lower())

def brute_force_decrypt(message):
    characters = "abcdefghijklmnopqrstuvwxyz,.!?'()0123456789 "

    with open("brute_force_decryptions.txt","w") as new_file:
        actual_decryption = ""
        actual_found = True
        for alpha_increment in range(1, 44):
            possible_decryption = ""
            for i in range(len(message)):
                alphabet_index = characters.index(message[i])
                new_index = (alphabet_index + alpha_increment) % 44
                possible_decryption += characters[new_index]
            new_file.write(possible_decryption + "\n")
            # split into words and check if all words with only letters are english words
            list = word_tokenize(possible_decryption)
            print(list)
            for item in list:
                if item.isalpha():
                    if not is_english_word(item): # if any word with letters is not an english word, this decryption cannot be the actual one
                        actual_found = False
            print(actual_found)
            if actual_found:
                actual_decryption = possible_decryption
        # print decryption message at bottom 
        new_file.write(f"\nThe actual decryption was found to be \"{actual_decryption}\"")

def is_english_word(word):
    return word in words.words()
    
main()