from function_class import number_is_palindrome

from unittest import TestCase

class TestClass(TestCase):

#    def test_that_number_is_palindrome(self):
#
#        palindrome = 1001
#        is_palindrome = number_is_palindrome(palindrome)
#
#        self.assertTrue(is_palindrome)
#

#    def test_that_number_is_not_prime(self):
#
#        prime_number = 8
#        is_prime = number_is_prime(prime_number)
#
#        self.assertFalse(is_prime)
#
#
#    def test_if_negative_number_is_prime(self):
#
#        prime_number = -11
#        is_prime = number_is_prime(prime_number)
#
#        self.assertTrue(is_prime)
#



 test_palindrome.py

def test_word_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False


def test_number_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(12321) is True
    assert is_palindrome(123) is False


def test_mixed_case_and_spaces():
    assert is_palindrome("Level") is True
    assert is_palindrome("nurses run") is True

