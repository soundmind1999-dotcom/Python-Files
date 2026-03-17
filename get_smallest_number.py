def smallest(lst):
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val


print("Smallest:", smallest([3, 7, 2, 9, 5]))
