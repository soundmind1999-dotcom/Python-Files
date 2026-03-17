def sum_first_middle_last(lst):
    num = len(lst)
    
    first = lst[0]
    last = lst[-1]
    
    if num % 2 == 1:
        middle = lst[num // 2]
    else:
        middle = (lst[num // 2 - 1] + lst[num // 2]) / 2
    
    return first + middle + last


print("Sum First, Middle, Last:", sum_first_middle_last([1,2,3,4,5]))
print("Even Case:", sum_first_middle_last([1,2,3,4]))
