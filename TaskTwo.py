number = int(input("Enter a number: "))

numberDigits = []

copyOfNumber = number

while (copyOfNumber != 0):
    numberDigits.append(copyOfNumber % 10)
    copyOfNumber //= 10

digitSquareSum = 0

for value in numberDigits:

    digitSquareSum += (value ** 2)

print(f"The sum of the square of each digit is {digitSquareSum}")

digitsFactorialSum = 0

for value in numberDigits:

    digitFactorial = 1

    for number in range (1, len(numberDigits) + 1):

        digitFactorial *= number
    digitsFactorialSum += digitFactorial

print(f"The sum of the factorial of each digit is {digitsFactorialSum}")

clonedNumberDigits = numberDigits.copy()
