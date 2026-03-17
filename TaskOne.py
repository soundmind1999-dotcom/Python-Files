listOfNumbers = []

for value in range (10):
    number = int(input(f"Enter number {value + 1}: "))
    listOfNumbers.append(number)
print()

evenNumbersSum = 0
oddNumbersSum = 0
print("The even numbers are:", end = " ")
for element in listOfNumbers:
    if (element % 2 == 0):
        print(element, end = " ")
        evenNumbersSum += element

print("\nThe odd numbers are:", end = " ")
for element in listOfNumbers:
    if (element % 2 != 0):
        print(element, end = " ")
        oddNumbersSum += element

print(f"\nThe sum of the even numbers is {evenNumbersSum}")
print(f"The sum of the odd numbers is {oddNumbersSum}")
print(f"The sum of the numbers is {oddNumbersSum + evenNumbersSum}")

oddNumbersSquareSum = 0
evenNumbersSquareSum = 0
print("The square of each even numbers are:", end = " ")
for element in listOfNumbers:
    if (element % 2 == 0):
        print(element * element, end = " ")
        evenNumbersSquareSum += (element * element)

print("\nThe square of each odd numbers are:", end = " ")
for element in listOfNumbers:
    if (element % 2 != 0):
        print(element * element, end = " ")
        oddNumbersSquareSum += (element * element)

print(f"\nThe mean of all the numbers is {(oddNumbersSum + evenNumbersSum)/10.0}")
print(f"The sum of the square of each even number is {evenNumbersSquareSum}")
print(f"The sum of the square of each odd number is {oddNumbersSquareSum}")
print(f"The sum of the square of each number is {oddNumbersSquareSum + evenNumbersSquareSum}")


