from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    result = ""
    for letter in text:
        if letter not in alphabet:
            result += letter
        else:
            result += (alphabet[(alphabet.index(letter) + shift) % 26])
    print("Your encoded text is:", result)


def decrypt(text, shift):
    result = ""
    for letter in text:
        if letter not in alphabet:
            result += letter
        else:
            result += (alphabet[(alphabet.index(letter) - shift) % 26])
    print("Your decoded text is:", result)


def caesar(text, shift, direction):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Provide correct data, text 'encode' or 'decode'\n")


print(logo)
restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(text, shift, direction)
    restart = input("Do you want to restart a program? Type 'yes' or 'no'\n").lower()

