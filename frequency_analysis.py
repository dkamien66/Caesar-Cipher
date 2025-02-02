# Load the encrypted string from the text file.
# Count how many times each letter occurs in the ciphertext, and find the letter that occurs most often.
# Use this information to calculate the key (assuming the most common letter corresponds to the letter E in plaintext).
# Decrypt the text using the key you calculated. Does the resulting plaintext make sense? If not, what do you think went wrong? 
# (hint: be careful with frequency analysis, E might not be the most common letter in individual sentences or short paragraphs)

def main():
    with open("coded_message.txt","r") as file:
        encryption = file.read()

    calculated_key = frequency_analysis(encryption.lower())
    print(f"The key is expected to be {calculated_key}.")

def frequency_analysis(encryption):
    alpha_dict = {}
    for i in range(len(encryption)):
        if encryption[i].isalpha():
            if encryption[i] not in alpha_dict:
                alpha_dict[encryption[i]] = 1
            else:
                alpha_dict[encryption[i]] += 1
        else:
            continue

    times_seen = 0
    most_common_letter = ""
    for letter, frequency in alpha_dict.items():
        if frequency > times_seen:
            times_seen = frequency
            most_common_letter = letter

    print(times_seen)
    print(most_common_letter)
    print(alpha_dict)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ((alphabet.index(most_common_letter) - 4) + 26) % 26
    return key

    


main()