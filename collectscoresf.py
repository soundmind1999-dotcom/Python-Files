def count_pass_fail():
    pass_count = 0
    fail_count = 0
    
    for count in range(1, 16):
        score = float(input(f"Enter the score for student {count}: "))
        
        if score >= 45:
            pass_count += 1
        else:
            fail_count += 1
    
    print("Number of students that passed:", pass_count)
    print("Number of students that failed:", fail_count)

count_pass_fail()

