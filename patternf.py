def print_pattern():
    for counter in range(5, 0, -1):
        for num in range(counter, 0, -1):
            print(num, end="")
        print()

print_pattern()

