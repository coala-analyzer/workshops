def reverse_words(string):
    """Reverse the words in a string."""
    pass  # TODO

from unittest import TestCase


class ReverseStringTestCase(TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "olleh")

    def test_simple_sentence(self):
        self.assertEqual(reverse_words("hello world"), "olleh dlrow")

    def test_sentence(self):
        self.assertEqual(reverse_words("Hello world - you're awesome!"),
                         "olleH dlrow - er'uoy emosewa!")
