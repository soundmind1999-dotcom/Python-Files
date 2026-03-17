total_bill = float(input("Enter total bill amount: "))
is_member = input("Are you a member? (yes/no): ")

if total_bill >= 1000 and is_member == "yes":
    discount = 0.10
    message = "10% discount applied for members"

elif total_bill >= 1000 and is_member != "yes":
    discount = 0.05
    message = "5% discount applied for non-members"
else:
    discount = 0
    message = "No discount applied."

discount_amount = total_bill * discount
final_amount = total_bill - discount_amount

print(message)
print(f"Final amount to pay: {final_amount:.2f}")
