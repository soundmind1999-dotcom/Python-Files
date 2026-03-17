#Types of Arguments
#
#Positional Arguments


def check_age(name, age, height):
    if age > 18:
        return f"{name} you are an Adult and your height is {height}"

    else: return f"{name} you are still a Child and your height is {height}"

#Positional Argument
print (check_age("Bright", 23, 1.5))

#Keyword Argument
#print (check_age(age=23, name="Bright", height=1.5))



#Default Argument

def check_age(name, age, height=3.2):
    if age > 18:
        return f"{name} you are an Adult and your height is {height}"

    else: return f"{name} you are still a Child and your height is {height}"

#Positional Argument
print (check_age("Bright", height=4.9, age=23))

#Keyword Argument
#print (check_age(age=23, name="Bright", height=1.5))



#Arbitary/Variable Length Arguments

def sum_all(*numbers):

        total = 0
        for number in numbers:
            total += number

        return total

print(sum_all(6,7,8,9,1,2,3,4,5,6,7,8,9,0))




#How to define a custom function
#naming onvention and indentation
#Functtion block and control statement suite
#function return and return keyord
#function with different types of argument


#Yet To Discuss - Read On These Tonight
#min and max inbuilt function
#Random number Generation
#Testing


#min inbuilt function

def lowest(num1, num2, num3, num4, num5, num6):
        return lowest


print(min(41,43,78,12,98,90))


































