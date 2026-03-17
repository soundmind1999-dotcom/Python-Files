


def sum_of_multiples_of_10():
    total = 0
    for number in range(1, 20001):
        if number % 10 == 0:
            total += number
    return total

print("Sum of multiples of 10 from 1 to 20000:", sum_of_multiples_of_10())

