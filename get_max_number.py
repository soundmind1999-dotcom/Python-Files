def largest(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


print("Largest:", largest([3, 7, 2, 9, 5]))
