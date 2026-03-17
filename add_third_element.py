def sum_every_third(lst):
    total = 0
    for value in range(2, len(lst), 3):
        total += lst[value]
    return total

print("Sum Every 3rd:", sum_every_third([1,2,3,4,5,6,7]))
