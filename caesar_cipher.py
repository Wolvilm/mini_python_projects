alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(word, jump, action):
    if action == 'encode':
        cipher_text = ""

        for letter in word:

            # Identify the position of the letter in the list of alphabets.
            position = alphabet.index(letter)
            # Determine the new index location after adding the shift number.
            new_position = position + jump
            number_of_letters = len(alphabet)

            # Dealing with a situation where we have to go past z and start over.
            if new_position > number_of_letters - 1:
                # Giving us how many places we should count from the beginning of the alphabet list.
                new_position -= number_of_letters
                new_letter = alphabet[new_position]
                cipher_text += new_letter

            else:
                new_letter = alphabet[new_position]
                cipher_text += new_letter

        print("The encoded output is {}".format(cipher_text))

    if direction == 'decode':
        decrypted_text = ""

        for letter in word:
            position = alphabet.index(letter)
            new_position = position - jump
            new_letter = alphabet[new_position]
            decrypted_text += new_letter

        print("The decoded output is {}".format(decrypted_text))


caesar(word=text, jump=shift, action=direction)
