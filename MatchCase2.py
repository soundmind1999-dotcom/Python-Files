#grade = int(input("Enter a grade: "))
#
#match grade:
#    case 80 | 90 | 100:
#        print("Excellent")
#    case 60 | 70:
#        print("Good")
#    case _:
#        print("Try harder")
#


choice = ""

while choice != "stop":
    score = int(input("Enter a score: "))

    match score:
        case 80:
            print("A")
        case 60:
            print("B")
        case 40:
            print("C")
        case 20:
            print("D")
        case 10:
            print("F")
        case 0:
            print("Stopping...")
            break
        case _:
            print("Invalid")

    choice = input("Do you want to enter another score? (type 'stop' to end): ")

