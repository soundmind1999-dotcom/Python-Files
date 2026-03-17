def multiply_third_positions(lst):
    result = 1
    for value in range(2, len(lst), 3):
        result *= lst[value]
    return result


print("Multiply Every 3rd:", multiply_third_positions([1, 2, 3, 4, 5, 6]))
