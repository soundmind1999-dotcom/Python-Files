grade = int(input("Enter a grade: "))

match grade:
    case 80 | 90 | 100:
        print("Excellent")
    case 60 | 70:
        print("Good")
    case _:
        print("Try harder")

