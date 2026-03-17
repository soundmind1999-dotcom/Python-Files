def sort_in_ascending_order(numbers):
    numbers.sort()
    return numbers


def only_even_numbers(numbers):
    even_numbers = []  
    for num in numbers:
        if num % 2 == 0:  
            even_numbers.append(num)
    return even_numbers


def combine_two_lists(a, b):
    return a + b

def words_more_than_three_characters(words):
    result = []
    for word in words:
        if len(word) > 3:
            result.append(word)
    return result


