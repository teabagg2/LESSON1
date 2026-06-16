# 1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.

v = 12
w = 8 
x = 4
y = 2
z = 0

z = (v + w) * x / y 
print(f"The value of z is: {z}")

name = "Alex"
age = 4
if name == "Alex" or (name == "John" and age >= 2):
    print("Welcome, Alex or John!")
else:
    print("Goodbye, not Alex or John!")
