def reverse_word(word):
    """Reverse the words in a string."""
    return "".join(rev.upper() if letter.isupper() else rev.lower()
                   for rev, letter in zip(reversed(word), word))

def reverse_words(sentence):
    return " ".join(reverse_word(word) for word in sentence.split())

from unittest import TestCase


class ReverseStringTestCase(TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "olleh")

    def test_cased_word(self):
        self.assertEqual(reverse_words("hEllo"), "oLleh")

    def test_simple_sentence(self):
        self.assertEqual(reverse_words("hello world"), "olleh dlrow")

    def test_sentence(self):
        self.assertEqual(reverse_words("Hello, world - you're awesome!"),
                         "Olleh, dlrow - er'uoy emosewa!")
