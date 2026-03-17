text = input("Enter a string: ")

vowels = "aeiouAEIOU"
position = -1

for i in range(len(text)):
    if text[count] in vowels:
        position = count
        break

if position != -1:
    print("First vowel found at position:", position)
else:
    print("No vowel found in the string.")
