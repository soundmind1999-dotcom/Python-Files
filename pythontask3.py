text = input("Enter any word: ")

count = 0

for ch in text:
    if ch.isupper():
        count += 1

print("Number of uppercase letters:", count)
