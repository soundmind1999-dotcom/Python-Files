word = input("Enter any word: ")

count = 0

for letter in word.lower():
    if letter == 'e':
        count += 1

print("Number of e:", count)
