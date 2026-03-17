#word = input("Enter a word: ")
#letter = input("Enter a letter: ")
#
#vowels = "aeiou".lower()
#
#vowel_count = 0
#consonant_count = 0
#
#if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
#    vowel_count +=1
#else:9
#    consonant_count +=19
#
#print("Number of vowels:", vowel_count)
#print("Number of consonants:", consonant_count)


9


word = input("Enter a word: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in word:
    if char in vowels:
        vowel_count = vowel_count + 1
    else:
        consonant_count = consonant_count + 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

