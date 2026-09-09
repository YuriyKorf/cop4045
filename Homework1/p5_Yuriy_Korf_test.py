"""Unit tests for the Caesar cipher program."""

import unittest

from p5_Yuriy_Korf import caesar_cipher, caesar_decipher, letter_frequency


class CaesarCipherTests(unittest.TestCase):
    def test_cipher_preserves_case_and_non_letters(self):
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

    def test_cipher_wraps_and_handles_negative_shifts(self):
        self.assertEqual(caesar_cipher("Zebra", 2), "Bgdtc")
        self.assertEqual(caesar_cipher("abc", -1), "zab")

    def test_decipher_returns_original_text(self):
        original = "Meet me at 5:30 PM."
        self.assertEqual(caesar_decipher(caesar_cipher(original, 10), 10), original)


class LetterFrequencyTests(unittest.TestCase):
    def test_frequency_ignores_case_and_non_letters(self):
        frequencies = letter_frequency("Apple! A2a")
        self.assertEqual(frequencies["a"], 3)
        self.assertEqual(frequencies["p"], 2)
        self.assertEqual(frequencies["l"], 1)
        self.assertEqual(frequencies["e"], 1)
        self.assertEqual(frequencies["z"], 0)

    def test_frequency_has_all_alphabet_letters(self):
        frequencies = letter_frequency("")
        self.assertEqual(len(frequencies), 26)
        self.assertTrue(all(count == 0 for count in frequencies.values()))


if __name__ == "__main__":
    unittest.main()
