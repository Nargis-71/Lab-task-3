name = input("Enter student's name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Number of characters:", len(name))
print("First character:", name[0] if name else "Empty name")
print("Last character:", name[-1] if name else "Empty name")
input()