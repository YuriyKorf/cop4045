"""Encrypt, decrypt, and analyze text with a Caesar cipher."""


def caesar_cipher(text, shift):
    """Return *text* with alphabetic characters shifted by *shift* places.

    Spaces, punctuation, and the case of every letter are preserved.
    """
    encrypted_text = ""
    shift = shift % 26

    for character in text:
        if "a" <= character <= "z":
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            position = alphabet.index(character)
            encrypted_text += alphabet[(position + shift) % 26]
        elif "A" <= character <= "Z":
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            position = alphabet.index(character)
            encrypted_text += alphabet[(position + shift) % 26]
        else:
            encrypted_text += character

    return encrypted_text


def caesar_decipher(cyphertext, shift):
    """Return the clear text obtained by reversing a Caesar cipher shift."""
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    """Return a dictionary containing the case-insensitive count of A through Z."""
    frequencies = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        frequencies[letter] = 0

    for character in text.lower():
        if character in alphabet:
            frequencies[character] += 1

    return frequencies


def display_frequency(frequencies):
    """Print a readable letter-frequency breakdown."""
    for letter in frequencies:
        print(f"{letter.upper()}: {frequencies[letter]}")


def main():
    """Run the terminal menu for the Caesar cipher program."""
    while True:
        print("\nCaesar Cipher Menu")
        print("1. Encrypt, analyze, and decipher a message")
        print("2. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            message = input("Enter a message: ")

            while True:
                try:
                    shift = int(input("Enter a shift value: "))
                    break
                except ValueError:
                    print("Please enter a whole number for the shift value.")

            cyphertext = caesar_cipher(message, shift)
            cleartext = caesar_decipher(cyphertext, shift)

            print(f"\nCiphered text: {cyphertext}")
            print("\nLetter frequency breakdown:")
            display_frequency(letter_frequency(message))
            print(f"\nDeciphered text: {cleartext}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
