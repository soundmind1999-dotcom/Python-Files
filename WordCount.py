#word = "semicolon"
#
#reverse = " "
#
#length_of_word = 0
#for letter in word:
#    print(letter, end ="\t")
#    reverse = letter + reverse
#    length_of_word += 1
#
#print()
#print(reverse, end = "\t")



#You cannot iterate through numbers
#range
#
#
#for i in range(5)
#output (0,1,2,3,4)
#for i in range(2, 10)
#output (2,3,4,5,6,7,8,9)
#
#write a loop that runs from 1-10

#for numbers in range(1,12, 3):

#first arg is start (default is 0)
#second arg is stop
#third arg is step (default is 1)

#for numbers in range(10,0, -2):
#   
#    print(numbers, end = " ")



#
#for numbers in range(6):
#    total = 0
#    total = total + numbers



#
#sum = 0
#for number in range(10):
#    sum += number
#    result = f"The sum of the sequence is: {sum} of the collection"
#    print(result)
#



#name = "Christopher"
#
#age = 54
#
#report = f"The student's name is {name} and his age is {age}"
#
#print(report)
#
#
#print("The student's name is", name, "and his age is", age)
#






#
#multiplier = 3
#
#
#for number in range(1, 13):
#
#
#    print(f"{multiplier} X {number} = {multiplier * number}")


#
#for multiplier in range(1,11):
#    for number in range (1,6):
#            result = f"{multiplier} X {number} = {multiplier * number}"
#            print(result, end='\t') #end=f"{'':>4}")
#
#    print()
#
#
#print()
#print()
#
#
#for multiplier in range(1,11):
#    for number in range (6,11):
#            result = f"{multiplier} X {number} = {multiplier * number}"
#            print(result, end='\t') #end=f"{'':>4}")
#
#
#    print()
#








#
#Break Staement
#
#for number in range(100):
#    if number == 10:
#        break
#    print(number, end='')
#
#
#Continue Statement

#
#for number in range(10):
#    if number % 2 == 0:
#        continue
#    print(number, end='')









count = 1 
while count <= 20:

    if count == 10:
        break

    print("The number is :", count)
    count += 1


