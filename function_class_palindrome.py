#Two fuctions - one of them takes in a number and returns if it is a prime number while the second one takes in a number and returns if it is a palindrome


#
#
#def number_is_prime(number):
#    if number < 0:
#        number *=-1
#
#    factors = 0
#    counter = 2
#    while(counter < number):
#        if number % counter == 0:
#            factors +=1
#        counter+=1
#    if factors == 0:
#        return True
#    return False
#
#
#
#def number_is_prime(number):
#
#    factors = 0
#    counter = 2
#    while(counter < number):
#        if number % counter == 0:
#            factors +=1
#        counter+=1
#    if factors == 0:
#        return True
#    return False



# palindrome.py

def is_palindrome(value):
    value = str(value).lower().replace(" ", "")
    return value == value[::-1]

