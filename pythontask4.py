text = input("Enter any word: ")

count = 0

for ch in text:
    if ch.islower():
        count += 1

print("Number of lowercase letters:", count)
