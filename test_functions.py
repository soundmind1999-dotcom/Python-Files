from function_class import number_is_prime

from unittest import TestCase

class TestClass(TestCase):

    def test_that_number_is_prime(self):

        prime_number = 11
        is_prime = number_is_prime(prime_number)

        self.assertTrue(is_prime)


    def test_that_number_is_not_prime(self):

        prime_number = 8
        is_prime = number_is_prime(prime_number)

        self.assertFalse(is_prime)


    def test_if_negative_number_is_prime(self):

        prime_number = -11
        is_prime = number_is_prime(prime_number)

        self.assertTrue(is_prime)


    


    

