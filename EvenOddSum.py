


sum_even= 0
sum_odd = 0
count = 0

while count < 20:
    num = int(input("Enter number count: ",))
    
    count += 1 
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
  

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd,)
