#word = input("Enter a word: ")
#number = int(input("Enter a number: "))
#result = ""
#
#for char in word:
#    result = result + (char * number)
#
#print(result)




def multiply_characters(word, number):
    result = ""

    for char in word:
        result += char * number

    return result


print(multiply_characters("car", 3))
