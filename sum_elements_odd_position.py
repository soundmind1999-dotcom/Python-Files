def sum_odd_positions(lst):
    total = 0
    for value in range(1, len(lst), 2):
        total += lst[value]
    return total


print("Odd Position Sum:", sum_odd_positions([1, 2, 3, 4, 5]))
