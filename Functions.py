#FUNCTIONS



#How to define a custom function
#naming onvention and indentation
#Functtion block and control statement suite
#function return and return keyord
#function with different types of argumnet
#min and max inbuilt function
#Random number Generation
#Testing

#keyword for function is def(define)

#arguments are the values
#parameter are the placeholders


#Design Thinkinng

#def add(first_number, second_number, third_number):
#        total = first_number + second_number + third_number
#        return first_number + second_number + third_number
#        return total
#
#print(add(6,5,8))
#
#def get_average(first_number, second_number, third_number):
#        summation = first_number + second_number+ third_number
#        return summation / 3
#
#def multiply(first_number, second_number, third_number):
#        multiply = first_number * second_number * third_number
#        return first_number * second_number * third_number
#        return multiply
#
#print(multiply(4,1,3))
#
#def get_square(number):
#
#        return number * number
#
#def get_sum_of_square(first_square, second_square, third_square):
#        return add(first_square, second_square, third_square)
#
#
#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second number: "))
#third_number = int(input("Enter third number: "))
#
#summation = add(first_number, second_number, third_number)
#average = get_average(first_number, second_number, third_number)
#product = multiply (first_number, second_number, third_number)
#square_of_the_sum = get_sum_of_square(first_square, second_square, third_square)
#
#print(f"The sum is: {summation}")
#print(f"The average is: {average}")
#print(f"The product is: {product}")
#





#print(f"The square of the sum is: {square_of_the_sum9}")

#def get_average_of_square(first_square, second_square, third_square):
#        return add(first_square, second_square, third_square)
#
#
#def get_product_of_square(first_square, second_square, third_square):
#        return add(first_square, second_square, third_square)

#function overshadowing
#your own will overshadow the inbuilt 



#The line of code under your control statement is called suite















def add(first_number, second_number, third_number):
    return first_number + second_number + third_number


def get_average(first_number, second_number, third_number):
    summation = first_number + second_number + third_number
    return summation / 3


def multiply(first_number, second_number, third_number):
    return first_number * second_number * third_number


def get_square(number):
    return number * number


def get_sum_of_square(first_square, second_square, third_square):
    return add(first_square, second_square, third_square)

def get_average_of_square(first_square, second_square, third_square):
    add = (first_square + second_square + third_square)
    return add / 3

def get_product_of_square(first_square, second_square, third_square):
    return (first_square * second_square * third_square)


# USER INPUT
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

# CALCULATIONS
summation = add(first_number, second_number, third_number)
average = get_average(first_number, second_number, third_number)
product = multiply(first_number, second_number, third_number)

# SQUARES
first_square = get_square(first_number)
second_square = get_square(second_number)
third_square = get_square(third_number)

# SUM OF SQUARES
sum_of_square = get_sum_of_square(first_square, second_square, third_square)

product_of_square = get_product_of_square(first_square, second_square, third_square)

average_of_square = get_average_of_square(first_square, second_square, third_square)

# OUTPUT 
print(f"The sum is: {summation}")
print(f"The average is: {average}")
print(f"The product is: {product}")
print(f"The sum of the squares is: {sum_of_square}")
print(f"The product of the squares is: {product_of_square}")
print(f"The average of the squares is: {average_of_square}")























