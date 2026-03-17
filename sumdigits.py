number = input("Enter a number: ")
total = 0

for digit in number:
    if digit.isdigit():   
        total += int(digit)

print(total)
