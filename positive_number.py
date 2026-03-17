number = int(input("Enter a positive number: "))


if number <= 0:
    print("Please enter a positive number.")
else:
    steps = 0
    print("Steps:")

    while number != 1:
        if number % 2 == 0:     
            number = number // 2
        else:                    
            number = (number // 3) + 1

        steps += 1
        print(f"Step {steps}: {number}")

    print("Total steps taken:", steps)
