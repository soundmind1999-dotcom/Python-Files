import random

def generate_random_list():
    numbers = []
    for _ in range(10):
        numbers.append(random.randint(1, 50))
    return numbers

# Test
print("Random List:", generate_random_list())
