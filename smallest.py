number = input("Enter a number: ")
smallest = 0

for digit in number:
    if digit.isdigit():          
        if int(digit) > smallest:
            smallest = int(digit)

print(smallest)
