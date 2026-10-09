numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Sum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Even numbers:", even)
print("Odd numbers:", odd)
input()