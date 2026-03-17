weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("BMI:", round(bmi, 2))
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("BMI:", round(bmi, 2))
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("BMI:", round(bmi, 2))
    print("Overweight")
else:
    print("BMI:", round(bmi, 2))
    print("Obese")
