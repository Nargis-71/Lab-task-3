total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = (total / 500) * 100

print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")

if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
    input()