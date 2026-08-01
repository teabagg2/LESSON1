# Loop Art Designer

# Step 1: Star Pyramid Section
print("=== Star Pyramid Pattern ===")

rows = int(input("Enter the number of rows for the star pyramid: "))

# Step 2 & 3: Nested loops and end=""
for i in range(1, rows + 1):
    # Print spaces before stars
    for j in range(rows - i):
        print(" ", end="")
    
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    # Move to next row
    print()


# Step 4 & 5: Floyd's Triangle
print("\n=== Floyd's Triangle ===")

rows = int(input("Enter the number of rows for Floyd's Triangle: "))

number = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()


# Step 6: Diamond Pattern
print("\n=== Diamond Pattern ===")

diamond_rows = int(input("Enter the diamond row size: "))

# Determine half rows
if diamond_rows % 2 == 0:
    half_rows = diamond_rows // 2
else:
    half_rows = diamond_rows // 2 + 1


# Step 7 & 8: Upper Half of Diamond
for i in range(1, half_rows + 1):
    # Leading spaces
    for j in range(half_rows - i):
        print(" ", end="")
    
    # Stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()


# Lower Half of Diamond
for i in range(half_rows - 1, 0, -1):
    # Leading spaces
    for j in range(half_rows - i):
        print(" ", end="")
    
    # Stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()


print("\n=== Loop Art Designer Complete ===")