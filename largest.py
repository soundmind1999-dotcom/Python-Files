number = input("Enter a number: ")
largest = 0

for digit in number:
    if digit.isdigit():          
        if int(digit) > largest:
            largest = int(digit)

print(largest)
