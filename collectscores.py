pass_counter = 0
fail_counter = 0

for count in range(1, 16):
    score = float(input(f"Enter the score of student {count}:"))
    
    if score >= 45:
        pass_counter += 1
    else:
        fail_counter += 1

print("Number of students that passed:", pass_counter)
print("Number of students that failed:", fail_counter)

