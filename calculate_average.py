def average(lst):
    total = 0
    count = 0
    for num in lst:
        total += num
        count += 1
    return total / count if count != 0 else 0


print("Average:", average([2, 4, 6, 8]))
