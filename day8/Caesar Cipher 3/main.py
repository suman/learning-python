# TODO-1: Import and print the logo from art.py when the program starts.

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    not_alphabet = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        try:
            index = alphabet.index(letter)
        except ValueError:
            index = -1

        if index <= -1:
            not_alphabet += letter
        else:
            shifted_position = index + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text + not_alphabet}")

    if not_alphabet != "":
        restart_program = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        if restart_program == 'yes':
            direction_again = input("Type 'encode to encrypt' 'decode to decrypt'")
            print(f"encoded text {output_text}")
            caesar(original_text=output_text, shift_amount=shift_amount, encode_or_decode=direction_again)


# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



