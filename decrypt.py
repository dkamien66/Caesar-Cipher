# Load the encrypted string from the text file.
# Try all 25 possible keys to decrypt the ciphertext, saving each result in a new string.
# Look at all 25 resulting strings. Most of them should be gibberish. Do any of them make sense? Can you figure out which one was the correct key?


def main():
    with open("coded_message.txt","r") as file:
        coded_message = file.read()

    brute_force_decrypt(coded_message.lower())

def brute_force_decrypt(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    with open("brute_force_decryptions.txt","w") as new_file:
        for alpha_increment in range(1, 26):
            possible_decryption = ""
            for i in range(len(message)):
                if message[i].isalpha():
                    alphabet_index = alphabet.index(message[i])
                    new_index = (alphabet_index + alpha_increment) % 26
                    possible_decryption += alphabet[new_index]
                else:
                    possible_decryption += message[i]
                    continue
            new_file.write(possible_decryption + "\n")
    
main()