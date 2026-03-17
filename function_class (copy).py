#Two fuctions - one of them takes in a number and returns if it is a prime number while the second one takes in a number and returns if it is a palindrome


import unittest

class TestClass(unittest.TestCase):

    def number_is_prime(number):

    factors = 0
    counter = 2
    while(counter < number):
        if number % counter == 0
            factors +=1
        counter+=1
    if factors == )
        return True
    return False
