def temperature_converter(celsius):

    fahrenheit = (celsius * 9/5) + 32

    return float(fahrenheit)

print (temperature_converter(22))





def calaculate_factorial(number):

    result = 1
    for value in range (1, number+1):

        result *= value

    return result

print (calaculate_factorial(4))

    
