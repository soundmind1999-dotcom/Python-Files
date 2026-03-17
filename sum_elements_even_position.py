def sum_even_positions(lst):
    total = 0
    for value in range(0, len(lst), 2):
        total += lst[value]
    return total


print("Even Position Sum:", sum_even_positions([1, 2, 3, 4, 5]))
