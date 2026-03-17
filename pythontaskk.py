
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def divide(num1, num2):
    if num2 == 0:
        print("Math Error:")
        return 0

    count = 0
    temp = num1  

    while num1>=num2:
        num1 = num1 - num2
        count++

    return count

result = divide(num1, num2)
print(result)
