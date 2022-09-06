alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(word, jump, action):
    if action == 'encode':
        cipher_text = ""

        # assigning variable for neatness
        number_of_letters = len(alphabet)

        # watching out for situation where shift is greater than number of alphabet letters.

        for char in word:
            if char in alphabet:
                # Identify the position of the letter in the list of alphabets.
                position = alphabet.index(char)

                if jump > len(alphabet):
                    new_position = position + (jump % len(alphabet))
                else:
                    new_position = position + jump

                # Dealing with a situation where we have to go past z and start over.
                if new_position > number_of_letters - 1:
                    # Giving us how many places we should count from the beginning of the alphabet list.
                    new_position -= number_of_letters
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter

                else:
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter

            # Takes care of characters not in alphabet
            else:
                cipher_text += char

        print("The encoded output is {}".format(cipher_text))

    if action == 'decode':
        decrypted_text = ""

        for char in word:
            if char in alphabet:
                position = alphabet.index(char)

                # handling case where shift is greater than number of letters in alphabet.
                if jump > len(alphabet):
                    new_position = position - (jump % len(alphabet))
                else:
                    new_position = position - jump

                new_letter = alphabet[new_position]
                decrypted_text += new_letter

            else:
                decrypted_text += char

        print("The decoded output is {}".format(decrypted_text))


caesar(word=text, jump=shift, action=direction)

run_again = (input("Would you like to run again? Type 'yes' or 'no': ")).lower()

while run_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(word=text, jump=shift, action=direction)
    run_again = (input("Would you like to run again?. Type 'yes to continue or anything else to end: ")).lower()
