def alphabet_position(letter):
    lower_letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.find(lower_letter)

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        char_index = alphabet_position(char)
        new_char_index = (char_index + rot) % 26
        new_char = alphabet[new_char_index]

        if char.isupper():
            new_char = new_char.upper()
    else:
        return char

    return new_char

def encrypt(text, rot):
    encrypted_text = ""
    for char in text:
        new_char = rotate_character(char, rot)
        encrypted_text += new_char

    return encrypted_text
